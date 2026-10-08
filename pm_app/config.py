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
STORAGE_MODE = os.environ.get("PM_MINDENES_STORAGE", "file").strip().lower()
if STORAGE_MODE not in ("file", "session"):
    STORAGE_MODE = "file"

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
