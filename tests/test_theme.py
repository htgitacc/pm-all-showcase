"""Az arculat: a színek olvashatók (WCAG AA, számolva), a téma és a modul ugyanazt mondja, a sávok a
tartalomból számolnak és escape-elnek, és minden fázis a saját színét kapja."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from pm_app import content, theme

CONFIG = Path(__file__).resolve().parent.parent / ".streamlit" / "config.toml"


def _luminance(color: str) -> float:
    channels = [int(color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    light, dark = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def test_contrast_formula_matches_the_wcag_reference_values():
    assert round(contrast("#000000", "#ffffff"), 1) == 21.0
    assert round(contrast("#777777", "#ffffff"), 2) == 4.48  # a klasszikus „épp nem AA” szürke


@pytest.fixture(scope="module")
def config() -> dict:
    return tomllib.loads(CONFIG.read_text(encoding="utf-8"))["theme"]


def test_config_theme_and_module_agree(config):
    assert config["primaryColor"] == config["linkColor"] == theme.ACCENT
    assert config["textColor"] == theme.TEXT
    assert config["backgroundColor"] == theme.BACKGROUND
    assert config["base"] == "light" and "dark" not in tomllib.loads(CONFIG.read_text(encoding="utf-8"))


def test_text_is_comfortably_readable_on_every_surface(config):
    # a folyó szöveg AAA-szinten (≥ 7:1) a háttéren, az oldalsávon és a kártyán
    for surface in (theme.BACKGROUND, config["secondaryBackgroundColor"], theme.CARD, theme.ACCENT_SOFT):
        assert contrast(theme.TEXT, surface) >= 7, surface
    sidebar = tomllib.loads(CONFIG.read_text(encoding="utf-8"))["theme"]["sidebar"]["backgroundColor"]
    assert contrast(theme.TEXT, sidebar) >= 7
    # a jelvények és az info-doboz szövege a saját hátterén AA
    for name in ("blue", "red", "orange"):
        assert contrast(config[f"{name}TextColor"], config[f"{name}BackgroundColor"]) >= 4.5, name


def test_accent_phase_and_hero_colors_carry_white_text_and_stand_on_the_background():
    colors = [theme.ACCENT, *theme.HERO, *theme.PHASE_COLORS.values()]
    for color in colors:
        assert contrast(color, "#ffffff") >= 4.5, color
    for color in [theme.ACCENT, *theme.PHASE_COLORS.values()]:
        assert contrast(color, theme.BACKGROUND) >= 4.5, color


def test_every_phase_has_its_own_color():
    numbers = [p["number"] for p in content.load_phases()]
    assert sorted(theme.PHASE_COLORS) == numbers
    assert len(set(theme.PHASE_COLORS.values())) == len(numbers)
    assert all(theme.phase_color(n) == theme.PHASE_COLORS[n] for n in numbers)


def test_css_highlights_cards_gates_and_teaching_boxes():
    numbers = [p["number"] for p in content.load_phases()]
    css = theme.css(numbers)
    for n in numbers:
        assert re.search(rf"\.st-key-fazis-kartya-{n} \{{ border-top: 5px solid {theme.PHASE_COLORS[n]}", css)
        assert re.search(rf"\.st-key-fazis-kapu-{n} \{{ border-left: 6px solid {theme.PHASE_COLORS[n]}", css)
    blockquote = css.split("blockquote {", 1)[1].split("}", 1)[0]
    assert theme.ACCENT in blockquote and "opacity: 1" in blockquote  # a Streamlit 0,6-ra halványítaná


def test_bands_escape_their_text():
    hero = theme.hero_html("<b>Cím</b>", "a & b", [(3, "<i>x</i>")])
    band = theme.phase_band_html(2, "<script>", "A&B", '"idéző"')
    for raw in ("<b>Cím</b>", "<i>x</i>", "<script>"):
        assert raw not in hero + band
    assert "&lt;b&gt;Cím&lt;/b&gt;" in hero and "a &amp; b" in hero and "A&amp;B" in band


def _html(at) -> list[str]:
    return [element.proto.body for element in at.get("html")]


def _container_keys(at) -> list[str]:
    """A `st.container(key=…)` kulcsai — ezekből lesz a `.st-key-…` CSS-osztály."""
    keys = []

    def walk(node):
        block_id = str(getattr(getattr(node, "proto", None), "id", ""))
        if match := re.search(r"-(fazis-[a-z]+-\d+)$", block_id):
            keys.append(match[1])
        children = getattr(node, "children", None)
        for child in children.values() if isinstance(children, dict) else []:
            walk(child)

    walk(at._tree)
    return keys


def test_overview_hero_counts_come_from_the_content(tmp_progress):
    at = AppTest.from_string("from pm_app import views\nviews.overview()\n", default_timeout=60).run()
    assert not at.exception
    blocks = _html(at)
    hero = next(b for b in blocks if 'class="pm-hero"' in b)
    phases = content.load_phases()
    expected = {
        "fázis": len(phases),
        "lépés": sum(len(p["checklist"]) for p in phases),
        "kitöltött minta": len(content.load_doc_index()),
        "mintaprojekt": len(content.sample_projects()),
    }
    assert expected == {"fázis": 6, "lépés": 85, "kitöltött minta": 69, "mintaprojekt": 2}
    for label, n in expected.items():
        assert f"<b>{n}</b> {label}</span>" in hero
    assert _container_keys(at) == [f"fazis-kartya-{p['number']}" for p in phases]
    heads = [b for b in blocks if "pm-card-head" in b]
    assert [re.search(r"background:(#[0-9a-f]{6})", h)[1] for h in heads] == [theme.PHASE_COLORS[p["number"]] for p in phases]


@pytest.mark.parametrize("phase_id", ["initiation", "planning", "execution", "monitoring", "closure", "benefits"])
def test_phase_page_opens_with_its_colored_band(phase_id, tmp_progress):
    script = f"from pm_app import views\nviews.make_phase_view({phase_id!r})()\n"
    at = AppTest.from_string(script, default_timeout=60).run()
    assert not at.exception
    phase = content.phase_by_id(phase_id)
    band = next(b for b in _html(at) if 'class="pm-band"' in b)
    assert f"background:{theme.PHASE_COLORS[phase['number']]}" in band
    assert f"<h1>{phase['title_hu']}</h1>" in band
    assert _container_keys(at) == ([f"fazis-kapu-{phase['number']}"] if phase.get("gate") else [])
