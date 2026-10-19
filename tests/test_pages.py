"""Füstteszt: minden oldal kivétel nélkül lefut, a letöltési csomag teljes."""

from __future__ import annotations

import io
import zipfile

import pytest
from streamlit.testing.v1 import AppTest

from pm_app import config, content, downloads, render

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


def test_narrow_screen_tables_scroll_instead_of_overflowing(tmp_progress):
    """Mobilon a széles mintadokumentum-tábla saját görgetést kap, a kártyán belüli címek kisebbek
    (különben szó közben törnek); asztalon nem változik semmi (csak a médialekérdezésen belül)."""
    css = render.NARROW_SCREEN_CSS
    body = css.split("@media (max-width: 640px) {", 1)[1]
    assert '[data-testid="stMarkdownContainer"] table' in body and "overflow-x: auto" in body
    for heading in ("h1", "h2", "h3"):
        assert f'[data-testid="stExpander"] [data-testid="stMarkdownContainer"] {heading} {{ font-size:' in body
    assert css.split("@media", 1)[0].strip() == "<style>", "médialekérdezésen kívüli szabály az asztalt is érintené"
    at = AppTest.from_file("../app.py", default_timeout=60).run()
    assert any(css in str(getattr(el.proto, "body", "")) for el in at.get("html")), "a CSS nincs az oldalon"


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
    "sample_project": 4,   # két mintaprojekt × (alapadatok, szerepkörök)
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


# ------------------------------------------------------------------ második mintaprojekt a felületen


def test_sample_project_page_has_one_tab_per_project(tmp_progress):
    at = _run("from pm_app import views\nviews.sample_project()\n")
    assert not at.exception, at.exception
    names = [p["name"] for p in content.sample_projects()]
    assert [t.label for t in at.tabs if t.label in names] == names   # a belső „Olvasható" fülek nem számítanak
    assert at.title[0].value == "Mintaprojektek"


def test_document_card_offers_both_examples_only_where_both_exist(tmp_progress):
    initiation = _run("from pm_app import views\nviews.make_phase_view('initiation')()\n")
    planning = _run("from pm_app import views\nviews.make_phase_view('planning')()\n")
    assert not initiation.exception, initiation.exception
    assert len(initiation.radio) == 11                        # az 1. fázis mind a 11 dokumentumához két példa
    assert len(planning.radio) == 0                           # a többi fázisban csak a Xyo-minta van
    first = initiation.radio[0]
    assert first.options == ["Xyo", "Kőris"] and first.value == "xyo"   # megjelenített (rövid) nevek; az érték az azonosító


def test_choosing_the_second_example_shows_its_sample(tmp_progress):
    at = _run("from pm_app import views\nviews.make_phase_view('initiation')()\n")
    at.radio(key="ex-project_idea").set_value("Kőris").run()
    at.toggle(key="show-project_idea").set_value(True).run()
    assert not at.exception, at.exception
    assert any("KTK-IK-001" in m.value for m in at.markdown)  # a Kőris-minta azonosítója
    assert not any("XYO-CP-001" in m.value for m in at.markdown)


def test_app_chrome_does_not_name_a_single_project():
    at = AppTest.from_file("../app.py", default_timeout=60).run()
    assert not at.exception, at.exception
    sidebar = " ".join(c.value for c in at.sidebar.caption)
    assert "Xyo" in sidebar and "Kőris" in sidebar          # mindkét példa, a meta.yaml-ból
    assert "Xyo Kft." not in at.main.caption[0].value       # az alcím projektsemleges
    assert "Xyo" not in config.APP_SUBTITLE


def test_no_hardcoded_company_name_in_the_app_code():
    # A mintaprojekt neve a meta.yaml-ból jön: a kódban sehol nem szerepelhet a Xyo Kft. felirata
    # (a menüben, az oldalsávban, a letöltési csomagban stb.). A Gantt és a PRINCE2-oldal szövege
    # kifejezetten a Xyo adatairól szól, ott a „Xyo" szó ("Xyo Cloud Pilot", "A Xyo projekten")
    # pontos jelölés, a cégnév teljes alakja viszont nem kell.
    for path in [config.ROOT / "app.py", *sorted((config.ROOT / "pm_app").glob("*.py"))]:
        assert "Xyo Kft" not in path.read_text(encoding="utf-8"), path.name


def test_second_example_zip_contains_exactly_its_samples():
    archive = zipfile.ZipFile(io.BytesIO(downloads.build_example_zip("koris")))
    names = archive.namelist()
    samples = [n for n in names if n != "OLVASSEL.txt"]
    assert len(samples) == len(downloads.example_docs("koris")) == 11
    assert all(n.startswith("1-initiation/koris-") for n in samples)   # ugyanaz a név, mint a kártyán
    readme = archive.read("OLVASSEL.txt").decode("utf-8")
    assert "Kőris Tervező Kft." in readme and all(n in readme for n in samples)
    assert "KTK-IK-001" in archive.read("1-initiation/koris-01-projekt-otlet.md").decode("utf-8")


def test_downloads_page_offers_the_second_example(tmp_progress):
    at = _run("from pm_app import views\nviews.downloads_page()\n")
    assert not at.exception, at.exception
    labels = [e.proto.label for e in at.get("download_button")]
    assert any(label.startswith("A Kőris-minták letöltése") for label in labels)
    assert any(label.startswith("Teljes csomag letöltése — Xyo") for label in labels)


def test_every_card_shows_its_koris_sample(tmp_progress):
    # Mind a 11 kártyán: a Kőris kiválasztva és megnyitva a saját (KTK-IK-0nn) mintáját mutatja.
    at = _run("from pm_app import views\nviews.make_phase_view('initiation')()\n")
    phase = content.phase_by_id("initiation")
    for number, doc in enumerate(phase["documents"], start=1):
        at.radio(key=f"ex-{doc['id']}").set_value("Kőris").run()
        at.toggle(key=f"show-{doc['id']}").set_value(True).run()
        assert not at.exception, (doc["id"], at.exception)
        assert any(f"KTK-IK-{number:03d}" in m.value for m in at.markdown), doc["id"]


def test_long_title_breaks_at_a_soft_hyphen_on_mobile(tmp_progress):
    # 390 px-en a „Dokumentumtérkép” 44 px-es címként nem fér ki (398 px > 358 px), és betűk
    # között törne; a feltételes elválasztójel (U+00AD) a szótagnál töri, asztalon láthatatlan.
    at = _run("from pm_app import views\nviews.doc_map()\n")
    assert at.title[0].value == "Dokumentum­térkép"
