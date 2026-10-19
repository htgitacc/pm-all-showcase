"""Az alkalmazás arculata: színek, a kezdőlap és a fázisoldal sávja, a kiemelések CSS-e.

A téma alapja a `.streamlit/config.toml` (kiemelőszín, szöveg, háttér, keret); ez a modul csak
azt adja hozzá, amit a téma nem tud: a fázisok saját színét, a sávokat és a tanítódobozok
kiemelését. Őszi, visszafogott színvilág egyetlen témában: meleg papírszín háttér (nem vakít,
és félhomályban sem kell hozzá sötét mód), sötétbarna szöveg, terrakotta kiemelés.
"""

from __future__ import annotations

import html

ACCENT = "#a14a2c"       # terrakotta: a kiemelőszín (= primaryColor a config.toml-ban)
ACCENT_SOFT = "#f6e8dd"  # a tanítódobozok és a kapu halvány háttere
CARD = "#faf7f2"         # a kártyák háttere, a papírszínnél egy árnyalattal világosabb
TEXT = "#2a2420"         # sötétbarna szöveg (= textColor)
BACKGROUND = "#f3eee7"   # meleg papírszín (= backgroundColor)
HERO = ("#8c3d24", "#a14a2c", "#a85a24")  # a kezdősáv színátmenete

# Az őszi lombok sora; mind ≥ 4,5:1 kontraszttal fehér szöveggel és a háttéren (a teszt számolja)
PHASE_COLORS = {
    1: "#9b3d2a",  # téglavörös
    2: "#9a4f12",  # rozsda
    3: "#7f5d10",  # okker
    4: "#5b6527",  # olíva
    5: "#6e4630",  # gesztenye
    6: "#7a2e44",  # szilva
}


def phase_color(number: int) -> str:
    return PHASE_COLORS.get(number, ACCENT)


def css(phase_numbers: list[int]) -> str:
    """A kiemelések stílusa. A fázis-kártyák és a kapu a `st.container(key=…)` osztályát kapják."""
    cards = "\n".join(
        f".st-key-fazis-kartya-{n} {{ border-top: 5px solid {phase_color(n)} !important; background: {CARD}; }}\n"
        f".st-key-fazis-kapu-{n} {{ border-left: 6px solid {phase_color(n)} !important; background: {ACCENT_SOFT}; }}"
        for n in phase_numbers
    )
    return f"""<style>
[data-testid="stMarkdownContainer"] blockquote {{
  border-left: 4px solid {ACCENT}; background: {ACCENT_SOFT};
  padding: .55rem 1rem; margin: .8rem 0; border-radius: 0 .5rem .5rem 0; color: {TEXT};
  opacity: 1;  /* a Streamlit 0,6-ra halványítja az idézetet */
}}
[data-testid="stMarkdownContainer"] blockquote :is(p, li, strong, em) {{ color: {TEXT}; }}
[data-testid="stMarkdownContainer"] blockquote p {{ margin: .25rem 0; }}
.pm-hero {{
  background: linear-gradient(120deg, {HERO[0]} 0%, {HERO[1]} 55%, {HERO[2]} 100%);
  color: #fff; border-radius: .9rem; padding: 1.6rem 1.8rem 1.4rem; margin-bottom: .6rem;
}}
.pm-hero h1 {{ color: #fff; margin: 0; padding: 0; font-size: 2.6rem; line-height: 1.15; }}
.pm-hero p {{ color: #fbefe6; margin: .35rem 0 1rem; font-size: 1.05rem; }}
.pm-kicker {{ font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; opacity: .85; }}
.pm-stats {{ display: flex; flex-wrap: wrap; gap: .5rem; }}
.pm-stat {{ background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.35);
  border-radius: 2rem; padding: .25rem .8rem; font-size: .95rem; }}
.pm-stat b {{ font-size: 1.1rem; }}
.pm-card-head {{ display: flex; align-items: center; gap: .6rem; }}
.pm-num {{ display: inline-flex; align-items: center; justify-content: center; flex: none;
  width: 2rem; height: 2rem; border-radius: 50%; color: #fff; font-weight: 700; }}
.pm-card-title {{ font-weight: 700; font-size: 1.05rem; color: {TEXT}; }}
.pm-band {{ display: flex; gap: 1rem; align-items: center; color: #fff;
  border-radius: .9rem; padding: 1.1rem 1.4rem; margin-bottom: .4rem; }}
.pm-band .pm-num {{ width: 3.2rem; height: 3.2rem; font-size: 1.6rem;
  background: rgba(255,255,255,.2); border: 2px solid rgba(255,255,255,.6); }}
.pm-band h1 {{ color: #fff; margin: 0; padding: 0; font-size: 2.1rem; line-height: 1.15; }}
.pm-band p {{ color: #fff; opacity: .92; margin: .2rem 0 0; }}
@media (max-width: 640px) {{
  .pm-hero {{ padding: 1.1rem 1.1rem 1rem; }}
  .pm-hero h1 {{ font-size: 1.9rem; }}
  .pm-band {{ padding: .9rem 1rem; gap: .75rem; }}
  .pm-band h1 {{ font-size: 1.5rem; }}
  .pm-band .pm-num {{ width: 2.5rem; height: 2.5rem; font-size: 1.25rem; }}
}}
{cards}
</style>"""


def hero_html(title: str, subtitle: str, stats: list[tuple[int, str]]) -> str:
    """A kezdőlap sávja: cím, alcím és a tartalomból számolt darabszámok."""
    chips = "".join(f'<span class="pm-stat"><b>{n}</b> {html.escape(label)}</span>' for n, label in stats)
    return (
        '<div class="pm-hero"><div class="pm-kicker">Waterfall · PMI/PMBOK</div>'
        f"<h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}</p>"
        f'<div class="pm-stats">{chips}</div></div>'
    )


def card_head_html(number: int, title: str) -> str:
    return (
        f'<div class="pm-card-head"><span class="pm-num" style="background:{phase_color(number)}">{number}</span>'
        f'<span class="pm-card-title">{html.escape(title)}</span></div>'
    )


def phase_band_html(number: int, title: str, title_en: str, tagline: str) -> str:
    """A fázisoldal fejléce a fázis színében."""
    return (
        f'<div class="pm-band" style="background:{phase_color(number)}"><span class="pm-num">{number}</span>'
        f'<div><div class="pm-kicker">{number}. fázis · {html.escape(title_en)}</div>'
        f"<h1>{html.escape(title)}</h1><p>{html.escape(tagline)}</p></div></div>"
    )
