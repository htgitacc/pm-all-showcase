"""A checklist pipáinak tárolása.

Két tárolási mód van (`config.STORAGE_MODE`):

- ``file`` (alapértelmezett, helyi használat): a pipák a `data/progress.json`
  fájlba mentődnek, tehát túlélik az újraindítást.
- ``session`` (nyilvános demó; Community Cloudon beállítás nélkül is): a pipák
  csak az adott böngészőmunkamenetben élnek, így a látogatók nem írják felül
  egymás haladását.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import date

import streamlit as st

from pm_app import config, content

WIDGET_PREFIX = "cb-"


def widget_key(item_id: str) -> str:
    return f"{WIDGET_PREFIX}{item_id}"


def persistent() -> bool:
    return config.STORAGE_MODE == "file"


def _load_from_disk() -> dict[str, bool]:
    if not config.PROGRESS_FILE.exists():
        return {}
    try:
        raw = json.loads(config.PROGRESS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return {k: bool(v) for k, v in raw.items()} if isinstance(raw, dict) else {}


def _write_to_disk(data: dict[str, bool]) -> None:
    """Ideiglenes fájlba ír, majd egy lépésben cseréli a haladásfájlt: egy írás
    közbeni leállás nem hagy félig megírt (érvénytelen JSON-) fájlt."""
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    tmp = config.PROGRESS_FILE.with_name(f"{config.PROGRESS_FILE.name}.{os.getpid()}.tmp")
    try:
        tmp.write_text(
            json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        os.replace(tmp, config.PROGRESS_FILE)
    finally:
        tmp.unlink(missing_ok=True)


def _persist(changes: dict[str, bool | None]) -> None:
    """Csak a megváltozott kulcsokat írja vissza a fájl friss állapotára.

    Így két nyitott böngészőfül nem írja felül egymás pipáit: mindegyik csak a
    saját módosítását viszi át. `None` érték = a kulcs törlése.
    """
    if not persistent():
        return
    data = _load_from_disk()
    for item_id, value in changes.items():
        if value is None:
            data.pop(item_id, None)
        else:
            data[item_id] = value
    _write_to_disk(data)


def state() -> dict[str, bool]:
    """A pipák állapota; az első hívásnál (fájl módban) fájlból töltjük be."""
    if "progress" not in st.session_state:
        st.session_state.progress = _load_from_disk() if persistent() else {}
    return st.session_state.progress


def toggle(item_id: str, key: str) -> None:
    """`st.checkbox` on_change callbackje: állapot frissítés + azonnali mentés."""
    value = bool(st.session_state[key])
    state()[item_id] = value
    _persist({item_id: value})


def is_done(item_id: str) -> bool:
    return state().get(item_id, False)


def _forget_widgets(item_ids) -> None:
    """A checkboxok saját widget-állapotát is töröljük, különben a következő
    futásban a régi (bejelölt) értékkel jelennének meg."""
    for item_id in item_ids:
        st.session_state.pop(widget_key(item_id), None)


def reset_phase(phase_id: str) -> None:
    phase = content.phase_by_id(phase_id)
    if not phase:
        return
    item_ids = [item["id"] for item in phase.get("checklist", [])]
    for item_id in item_ids:
        state().pop(item_id, None)
    _forget_widgets(item_ids)
    _persist({item_id: None for item_id in item_ids})


def reset_all() -> None:
    _forget_widgets(list(state()))
    st.session_state.progress = {}
    if persistent():
        _write_to_disk({})


# ----------------------------------------------------------- mentés és visszatöltés
# Demó módban a pipák a lap bezárásával elvesznek: a látogató JSON-fájlba mentheti és
# visszatöltheti őket. A feltöltött fájl kívülről jön, ezért mindent ellenőrzünk.

EXPORT_FORMAT = "pm-mindenes-haladas"
EXPORT_VERSION = 1
# A teljes checklist mentése néhány KB; ennél jóval nagyobb fájl biztosan nem mentés.
MAX_IMPORT_BYTES = 64 * 1024


class InvalidProgressFile(ValueError):
    """A feltöltött fájl nem használható haladásmentés; az üzenet a felhasználónak szól."""


@dataclass(frozen=True)
class ImportPreview:
    done: tuple[str, ...]      # a betöltendő, a checklistben létező azonosítók
    unknown: int               # a mentésben szereplő, de ma nem létező azonosítók száma
    exported: str              # a mentés dátuma (ISO), vagy üres, ha nem olvasható


def known_item_ids() -> set[str]:
    return {item["id"] for phase in content.load_phases() for item in phase.get("checklist", [])}


def build_export(done_ids, today: date) -> bytes:
    payload = {
        "format": EXPORT_FORMAT,
        "version": EXPORT_VERSION,
        "exported": today.isoformat(),
        "done": sorted(done_ids),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")


def export_json() -> bytes:
    return build_export((i for i, v in state().items() if v), date.today())


def parse_import(raw: bytes, known_ids: set[str]) -> ImportPreview:
    """Ellenőrzi a feltöltött mentést; hibánál `InvalidProgressFile`.

    Az ismeretlen azonosítókat (pl. egy régebbi tartalomverzióból) kihagyja, és csak a
    számukat adja vissza — a fájl szövege így nem kerül ki a felületre.
    """
    if len(raw) > MAX_IMPORT_BYTES:
        raise InvalidProgressFile("A fájl túl nagy ahhoz, hogy haladásmentés legyen.")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise InvalidProgressFile("A fájl nem érvényes JSON.") from None
    if not isinstance(data, dict) or data.get("format") != EXPORT_FORMAT:
        raise InvalidProgressFile("Ez a fájl nem PM-mindenes haladásmentés.")
    if data.get("version") != EXPORT_VERSION:
        raise InvalidProgressFile("A mentés ismeretlen verziójú.")
    done = data.get("done")
    if not isinstance(done, list) or not all(isinstance(i, str) for i in done):
        raise InvalidProgressFile("A mentésben a pipák listája hibás.")

    exported = data.get("exported")
    try:
        exported = date.fromisoformat(exported).isoformat() if isinstance(exported, str) else ""
    except ValueError:
        exported = ""
    ids = set(done)
    return ImportPreview(
        done=tuple(sorted(ids & known_ids)),
        unknown=len(ids - known_ids),
        exported=exported,
    )


def apply_import(preview: ImportPreview) -> None:
    """A mentett állapot felülírja az aktuálisat (visszaállítás, nem összefésülés)."""
    _forget_widgets(known_item_ids() | set(state()))
    st.session_state.progress = dict.fromkeys(preview.done, True)
    if persistent():
        _write_to_disk(dict(st.session_state.progress))


def phase_stats(phase: dict) -> dict:
    """Haladás egy fázisra: a kötelező elemek adják a fő százalékot."""
    items = phase.get("checklist", [])
    mandatory = [i for i in items if i.get("mandatory", True)]
    optional = [i for i in items if not i.get("mandatory", True)]

    done_m = sum(1 for i in mandatory if is_done(i["id"]))
    done_o = sum(1 for i in optional if is_done(i["id"]))

    return {
        "total": len(items),
        "done": done_m + done_o,
        "mandatory_total": len(mandatory),
        "mandatory_done": done_m,
        "optional_total": len(optional),
        "optional_done": done_o,
        "ratio": (done_m / len(mandatory)) if mandatory else 0.0,
    }


def overall_ratio() -> float:
    phases = content.load_phases()
    total = sum(phase_stats(p)["mandatory_total"] for p in phases)
    done = sum(phase_stats(p)["mandatory_done"] for p in phases)
    return (done / total) if total else 0.0
