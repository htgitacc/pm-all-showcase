"""Füstteszt: minden oldal kivétel nélkül lefut, a letöltési csomag teljes."""

from __future__ import annotations

import io
import zipfile

import pytest
from streamlit.testing.v1 import AppTest

from pm_app import content, downloads, render

PAGES = ["overview", "sample_project", "doc_map", "downloads_page", "glossary", "prince2"]
PHASES = ["initiation", "planning", "execution", "monitoring", "closure", "benefits"]


def _run(script: str) -> AppTest:
    return AppTest.from_string(script, default_timeout=60).run()


@pytest.mark.parametrize("page", PAGES)
def test_page_renders(page, tmp_progress):
    at = _run(f"from pm_app import views\nviews.{page}()\n")
    assert not at.exception, at.exception


@pytest.mark.parametrize("phase_id", PHASES)
def test_phase_page_renders(phase_id, tmp_progress):
    at = _run(f"from pm_app import views\nviews.make_phase_view({phase_id!r})()\n")
    assert not at.exception, at.exception


def test_full_app_renders(tmp_progress):
    at = AppTest.from_file("../app.py", default_timeout=60).run()
    assert not at.exception, at.exception


def test_full_zip_contains_every_sample():
    docs = downloads.all_docs_with_samples()
    archive = zipfile.ZipFile(io.BytesIO(downloads.build_zip(docs)))
    names = archive.namelist()
    assert len(docs) == len(content.load_doc_index())
    assert len(names) == len(set(names)) == len(docs) + 1  # + OLVASSEL.txt
    assert "OLVASSEL.txt" in names


# Az `st.dataframe` rács-alapú: a hosszú cellaszöveget nem tördeli, hanem levágja
# (a Mintaprojekt „Platform" és „Miért fontos" cellái így lógtak ki). A
# szöveges táblák ezért `st.table`-lel (render.text_table) jelennek meg; az
# `st.dataframe` csak a rövid Gantt-mérföldkő-táblának marad. A dokumentumleltár
# „Bemenete" / „Mihez bemenet" cellái akár 250 karakteresek, ezért az is tördel.
TEXT_TABLES = {
    "sample_project": 2,   # alapadatok, szerepkörök
    "prince2": None,       # fülenként: nem számoljuk, de nem lehet rács
    "doc_map": 1,          # a teljes dokumentumleltár
}


@pytest.mark.parametrize("page, expected", TEXT_TABLES.items())
def test_text_tables_wrap_instead_of_clipping(page, expected, tmp_progress):
    at = _run(f"from pm_app import views\nviews.{page}()\n")
    assert not at.exception, at.exception
    assert len(at.dataframe) == 0, f"{page}: rács-alapú tábla szöveges tartalommal"
    if expected is not None:
        assert len(at.table) == expected


@pytest.mark.parametrize("phase_id", PHASES)
def test_phase_text_tables_wrap_instead_of_clipping(phase_id, tmp_progress):
    at = _run(f"from pm_app import views\nviews.make_phase_view({phase_id!r})()\n")
    assert len(at.dataframe) == 0, f"{phase_id}: rács-alapú tábla szöveges tartalommal"


@pytest.mark.parametrize(
    "raw, shown",
    [
        ("1. Kezdeményezés", "1\\. Kezdeményezés"),  # különben <ol><li>Kezdeményezés</li></ol>
        ("12. pont", "12\\. pont"),
        ("- tétel", "\\- tétel"),
        ("Fázis 1. lépése", "Fázis 1. lépése"),       # csak a sor eleje lehet lista
        ("2026.03.13.", "2026.03.13."),
        (42, 42),
    ],
)
def test_table_cells_do_not_turn_into_markdown_lists(raw, shown):
    assert render.table_cell(raw) == shown


def test_doc_map_phase_column_is_not_a_numbered_list(tmp_progress):
    at = _run("from pm_app import views\nviews.doc_map()\n")
    phases = list(at.table[0].value["Fázis"])
    assert len(phases) == 69
    # escape-elt pont, utána nem törő szóköz: nem lista, és a szám nem törik külön sorba
    assert all(p[0].isdigit() and "\\.\u00a0" in p for p in phases), phases[:3]


def test_sidebar_starts_collapsed_on_mobile():
    # "expanded" mellett mobilon az oldalsáv első betöltéskor eltakarja a tartalmat;
    # "auto": asztalon nyitva, keskeny kijelzőn csukva.
    import ast

    tree = ast.parse((content.config.ROOT / "app.py").read_text(encoding="utf-8"))
    call = next(
        n for n in ast.walk(tree)
        if isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "set_page_config"
    )
    state = next(k.value.value for k in call.keywords if k.arg == "initial_sidebar_state")
    assert state == "auto"
