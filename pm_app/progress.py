"""A checklist pipáinak tárolása.

Két tárolási mód van (`config.STORAGE_MODE`):

- ``file`` (alapértelmezett, helyi használat): a pipák a `data/progress.json`
  fájlba mentődnek, tehát túlélik az újraindítást.
- ``session`` (nyilvános demó): a pipák csak az adott böngészőmunkamenetben
  élnek, így a látogatók nem írják felül egymás haladását.
"""

from __future__ import annotations

import json

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
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    config.PROGRESS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


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
