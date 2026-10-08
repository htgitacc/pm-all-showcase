"""Közös tesztsegédek: útvonal, markdown-táblák és forintösszegek olvasása."""

from __future__ import annotations

import logging
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# A Streamlit cache futtatókörnyezet nélkül figyelmeztet — a tesztekben ez zaj.
logging.getLogger("streamlit").setLevel(logging.ERROR)


def read_doc(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def section(text: str, heading_start: str) -> str:
    """Egy `## ...` / `### ...` szakasz szövege a következő azonos vagy magasabb szintű címig."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("#") and line.lstrip("#").strip().startswith(heading_start):
            level = len(line) - len(line.lstrip("#"))
            body = []
            for nxt in lines[i + 1 :]:
                if nxt.startswith("#") and len(nxt) - len(nxt.lstrip("#")) <= level:
                    break
                body.append(nxt)
            return "\n".join(body)
    raise AssertionError(f"Nincs ilyen szakasz: {heading_start!r}")


def tables(text: str) -> list[list[list[str]]]:
    """Az összes markdown-tábla a szövegben, fejléc és elválasztó sor nélkül."""
    result, current = [], []
    for line in text.splitlines() + [""]:
        if line.startswith("|"):
            current.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif current:
            rows = [r for r in current[2:] if r]  # fejléc + |---| elválasztó kihagyva
            result.append(rows)
            current = []
    return result


_FT = re.compile(r"[−-]?\d{1,3}(?:[  ]\d{3})+(?= Ft)|[−-]?\d+(?= Ft)")


def ft(cell: str) -> int | None:
    """Egy cella első forintösszege egész számként (`−860 000 Ft` → -860000)."""
    match = _FT.search(cell.replace("*", ""))
    if not match:
        return None
    raw = match.group(0).replace("−", "-").replace(" ", "").replace(" ", "")
    return int(raw)


def num(cell: str) -> float:
    """Magyar tizedesvesszős szám (`**1,03**` → 1.03)."""
    return float(cell.replace("*", "").replace(",", ".").strip())


@pytest.fixture
def tmp_progress(tmp_path, monkeypatch):
    """A haladásfájl átirányítása egy ideiglenes mappába, fájl módban."""
    from pm_app import config

    monkeypatch.setattr(config, "DATA_DIR", tmp_path)
    monkeypatch.setattr(config, "PROGRESS_FILE", tmp_path / "progress.json")
    monkeypatch.setattr(config, "STORAGE_MODE", "file")
    return tmp_path / "progress.json"
