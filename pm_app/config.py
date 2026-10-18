"""Központi útvonalak és konstansok."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIR = ROOT / "content"
PHASES_DIR = CONTENT_DIR / "phases"
META_FILE = CONTENT_DIR / "meta.yaml"
PRINCE2_FILE = CONTENT_DIR / "prince2.yaml"
DOCS_DIR = ROOT / "docs"
DATA_DIR = ROOT / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"

# A pipák tárolása: "file" (helyi, tartós) vagy "session" (nyilvános demó,
# látogatónként külön). Streamlit Community Cloudon a Secrets-ben megadott
# PM_MINDENES_STORAGE = "session" sor környezeti változóként érkezik.
STORAGE_MODES = ("file", "session")

# A Community Cloud a repót a /mount/src/<repó> alá klónozza.
CLOUD_SOURCE_ROOT = Path("/mount/src")


def storage_mode(environ=os.environ, root: Path = ROOT) -> str:
    """A tárolási mód: a környezeti változó dönt, ha érvényes.

    Ha hiányzik vagy elgépelt, a hely dönt: Community Cloudon "session",
    különben "file". Így egy kimaradt Secrets-sor miatt sem írja minden
    látogató ugyanazt a fájlt.
    """
    mode = environ.get("PM_MINDENES_STORAGE", "").strip().lower()
    if mode in STORAGE_MODES:
        return mode
    return "session" if root.is_relative_to(CLOUD_SOURCE_ROOT) else "file"


STORAGE_MODE = storage_mode()

APP_TITLE = "PM-mindenes"
APP_SUBTITLE = "Waterfall projektmenedzser checklist — Xyo Kft. mintaprojekttel"

# Jelölések a felületen
BADGE_MANDATORY = ":red-badge[kötelező]"
BADGE_OPTIONAL = ":gray-badge[ajánlott]"

# A PRINCE2-réteg jelölése — végig ugyanaz, hogy elváljon a PMI-gerinctől
BADGE_PRINCE2 = ":violet-badge[PRINCE2]"
PRINCE2_NOTE = (
    "Ez a blokk **módszertani kiegészítés**. A fázis PMI szerinti tartalmát "
    "nem módosítja — azt mutatja meg, hogyan nézne ki ugyanez PRINCE2-ben."
)

# A dokumentumkártyák magyarázata az "ajánlott" kategóriához
OPTIONAL_HINT = (
    "A gyakorlatban nem mindig készül el, de számonkérhető a PM-en — "
    "és ha elkészíted, téged véd."
)
