"""A README képernyőképeinek újragyártása — egységes méretben, egy paranccsal.

Headless Edge-et (vagy Chrome-ot) vezérel a DevTools-protokollon keresztül, a
Streamlit mellé telepített `websockets` csomaggal; új függőség nem kell.

Használat (előtte a demó szerver fusson, hogy a pipálás ne írjon fájlba):

    PM_MINDENES_STORAGE=session .venv/bin/streamlit run app.py --server.address 127.0.0.1 --server.port 8531
    .venv/bin/python tools/screenshots.py                    # → docs/screenshots/
    .venv/bin/python tools/screenshots.py --out kepek --only 06

Böngésző: a `--browser` kapcsoló, a BROWSER környezeti változó, vagy a szokásos
Edge/Chrome útvonalak közül az első létező.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import itertools
import json
import os
import shutil
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path

import websockets

ROOT = Path(__file__).resolve().parent.parent
WIDTH, HEIGHT = 1440, 1000
BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

# --------------------------------------------------------------------- a képek listája
# Minden lépés egy JavaScript-kifejezés, amely az oldalon fut; utána a szkript
# megvárja, amíg a Streamlit újra lefut. A checkboxot/kapcsolót a belső `input`-on
# kattintjuk: a Streamlit 1.66-ban a `label.click()` már nem váltja át.

def _click_label(text: str) -> str:
    return (
        "[...document.querySelectorAll('[data-testid=\"stCheckbox\"] label')]"
        f".find(l => l.innerText.includes({json.dumps(text)})).querySelector('input').click()"
    )


def _open_expander(text: str) -> str:
    return (
        "[...document.querySelectorAll('[data-testid=\"stExpander\"] summary')]"
        f".find(s => s.innerText.includes({json.dumps(text)})).click()"
    )


def _click_button(text: str) -> str:
    return (
        "[...document.querySelectorAll('[data-testid=\"stMain\"] button')]"
        f".find(b => b.innerText.trim() === {json.dumps(text)}).click()"
    )


def _toggle_in_expander(expander: str, toggle: str) -> str:
    return (
        "[...[...document.querySelectorAll('[data-testid=\"stExpander\"]')]"
        f".find(e => e.querySelector('summary').innerText.includes({json.dumps(expander)}))"
        f".querySelectorAll('label')].find(l => l.innerText.includes({json.dumps(toggle)}))"
        ".querySelector('input').click()"
    )


def _choose_in_expander(expander: str, option: str) -> str:
    """Egy rádiógomb-opció kiválasztása egy megnyitott kártyán belül (pl. a mintaprojekt)."""
    return (
        "[...[...document.querySelectorAll('[data-testid=\"stExpander\"]')]"
        f".find(e => e.querySelector('summary').innerText.includes({json.dumps(expander)}))"
        f".querySelectorAll('label')].find(l => l.innerText.trim() === {json.dumps(option)})"
        ".querySelector('input').click()"
    )


def _scroll_to(selector: str, text: str, offset: int = 24) -> str:
    return (
        f"(() => {{ const el = [...document.querySelectorAll({json.dumps(selector)})]"
        f".find(e => e.innerText.includes({json.dumps(text)}));"
        " el.scrollIntoView({block: 'start'});"
        " const main = document.querySelector('[data-testid=\"stMain\"]');"
        f" if (main) main.scrollBy(0, -{offset}); }})()"
    )


SHOTS = [
    {"file": "01-attekintes.png", "path": "/"},
    {
        "file": "02-checklist.png",
        "path": "/fazis-2-planning",
        "steps": [
            _click_label("1. Írd meg a Hatókör-nyilatkozatot"),
            _click_label("2. Tartsatok WBS-workshopot"),
            _click_label("5. Készítsd el az ütemtervet"),
            _scroll_to("h2, h3", "Checklist — a fázis lépései sorrendben"),
        ],
    },
    {
        "file": "03-dokumentumkartya.png",
        "path": "/fazis-2-planning",
        "steps": [
            _open_expander("Költségvetés és költségbázis"),
            _toggle_in_expander("Költségvetés és költségbázis", "Kitöltött minta megjelenítése"),
            _scroll_to("h1", "Költségvetés és költségbázis (Budget / Cost Baseline)", offset=60),
        ],
    },
    {"file": "04-dokumentumterkep.png", "path": "/dokumentumterkep"},
    {"file": "05-prince2.png", "path": "/prince2"},
    {
        "file": "06-gantt.png",
        "path": "/gantt",
        "steps": [_click_button("Csak a kritikus út"), _scroll_to("p, label", "Mit mutasson?", offset=90)],
    },
    {
        "file": "07-masodik-mintaprojekt.png",
        "path": "/fazis-1-initiation",
        "steps": [
            _open_expander("Üzleti indoklás"),
            _choose_in_expander("Üzleti indoklás", "Kőris"),
            _toggle_in_expander("Üzleti indoklás", "Kitöltött minta megjelenítése"),
            _scroll_to("p", "Melyik mintaprojektből?", offset=150),
        ],
    },
]

# ------------------------------------------------------------------ DevTools-vezérlés

READY = (
    "!!document.querySelector('[data-testid=\"stMain\"] h1, [data-testid=\"stMain\"] h2')"
    " && !document.querySelector('[data-testid=\"stStatusWidget\"]')"
    " && !document.querySelector('[data-testid=\"stSkeleton\"]')"
)


class Page:
    def __init__(self, ws):
        self.ws = ws
        self.ids = itertools.count(1)

    async def call(self, method: str, **params):
        msg_id = next(self.ids)
        await self.ws.send(json.dumps({"id": msg_id, "method": method, "params": params}))
        while True:
            reply = json.loads(await self.ws.recv())
            if reply.get("id") == msg_id:
                if "error" in reply:
                    raise RuntimeError(f"{method}: {reply['error']}")
                return reply.get("result", {})

    async def evaluate(self, expression: str):
        result = await self.call("Runtime.evaluate", expression=expression, awaitPromise=True, returnByValue=True)
        if "exceptionDetails" in result:
            raise RuntimeError(f"JavaScript-hiba: {result['exceptionDetails'].get('text')} — {expression[:80]}")
        return result.get("result", {}).get("value")

    async def settle(self, timeout: float = 30.0) -> None:
        """Megvárja, amíg a Streamlit lefut és a diagramok kirajzolódnak."""
        await asyncio.sleep(0.8)  # a kattintás utáni újrafutás elindulhasson
        deadline = time.monotonic() + timeout
        stable = 0
        while time.monotonic() < deadline:
            stable = stable + 1 if await self.evaluate(READY) else 0
            if stable >= 3:
                await asyncio.sleep(1.5)  # Vega- és Graphviz-rajzolás
                return
            await asyncio.sleep(0.4)
        raise TimeoutError("Az oldal nem állt össze időben")


def _find_browser(explicit: str | None) -> str:
    for candidate in [explicit, os.environ.get("BROWSER"), *BROWSERS]:
        if candidate and Path(candidate).exists():
            return candidate
    found = shutil.which("msedge") or shutil.which("chrome") or shutil.which("chromium")
    if not found:
        found = _playwright_chromium()
    if not found:
        raise SystemExit(
            "Nem találok Edge-et vagy Chrome-ot; add meg: --browser <útvonal>, "
            "vagy headless Linuxon: pip install playwright && playwright install chromium"
        )
    return found


PLAYWRIGHT_CACHE = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH") or Path.home() / ".cache" / "ms-playwright")


def _playwright_chromium() -> str | None:
    """A Playwright által letöltött Chromium (headless szerveren nincs rendszerböngésző).

    A headless shell az első választás: a teljes Chrome-nak grafikus rendszerkönyvtárak
    kellenének (libatk stb.), amelyek egy szerveren jellemzően hiányoznak.
    Csoportonként a legfrissebb build (a mappanév végi szám szerint)."""
    def build(path: Path) -> int:
        tail = path.parent.parent.name.rsplit("-", 1)[-1]
        return int(tail) if tail.isdigit() else 0

    for pattern in ("chromium_headless_shell-*/*/chrome-headless-shell",
                    "chromium_headless_shell-*/*/headless_shell",
                    "chromium-*/chrome-linux*/chrome"):
        found = sorted(PLAYWRIGHT_CACHE.glob(pattern), key=build)
        if found:
            return str(found[-1])
    return None


def _debugger_url(port: int) -> str:
    deadline = time.monotonic() + 20
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2) as resp:
                pages = [t for t in json.load(resp) if t.get("type") == "page"]
            if pages:
                return pages[0]["webSocketDebuggerUrl"]
        except OSError:
            pass
        time.sleep(0.3)
    raise SystemExit("A böngésző nem nyitotta meg a DevTools-portot")


def _launch_browser(browser: str, port: int) -> tuple[subprocess.Popen, str]:
    """A headless böngésző indítása — szinkron, az async rész előtt (a Popen és a
    DevTools-port várása blokkoló, az eseményhurokban nem futhat)."""
    profile = tempfile.mkdtemp(prefix="pm-screens-")
    # A Playwright-Chromiumot a Playwright is sandbox nélkül indítja: újabb Ubuntun
    # (AppArmor) a felhasználói névtér tiltva van, és enélkül el sem indul. Csak a
    # saját, helyben futó appot nyitja meg.
    no_sandbox = ["--no-sandbox"] if Path(browser).is_relative_to(PLAYWRIGHT_CACHE) else []
    proc = subprocess.Popen(
        [browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
         *no_sandbox,
         f"--remote-debugging-port={port}", f"--user-data-dir={profile}",
         f"--window-size={WIDTH},{HEIGHT}", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return proc, profile


def _stop_browser(proc: subprocess.Popen, profile: str) -> None:
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
    shutil.rmtree(profile, ignore_errors=True)


async def _capture(ws_url: str, base_url: str, out_dir: Path, shots: list[dict]) -> None:
    async with websockets.connect(ws_url, max_size=None) as ws:
        page = Page(ws)
        await page.call("Page.enable")
        await page.call("Emulation.setDeviceMetricsOverride", width=WIDTH, height=HEIGHT,
                        deviceScaleFactor=1, mobile=False)
        await page.call("Emulation.setEmulatedMedia",
                        features=[{"name": "prefers-color-scheme", "value": "light"}])
        for shot in shots:
            await page.call("Page.navigate", url=base_url.rstrip("/") + shot["path"])
            await page.settle()
            for step in shot.get("steps", []):
                await page.evaluate(step)
                await page.settle()
            data = await page.call("Page.captureScreenshot", format="png")
            target = out_dir / shot["file"]
            target.write_bytes(base64.b64decode(data["data"]))
            print(f"kész: {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", default="http://127.0.0.1:8531", help="a futó (demó módú) app címe")
    parser.add_argument("--out", default=str(ROOT / "docs" / "screenshots"), help="célmappa")
    parser.add_argument("--only", nargs="*", help="csak ezek a képek (fájlnév-előtag, pl. 06)")
    parser.add_argument("--browser", help="az Edge/Chrome futtatható fájlja")
    parser.add_argument("--port", type=int, default=9333, help="DevTools-port")
    args = parser.parse_args()

    shots = [s for s in SHOTS if not args.only or any(s["file"].startswith(p) for p in args.only)]
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    proc, profile = _launch_browser(_find_browser(args.browser), args.port)
    try:
        asyncio.run(_capture(_debugger_url(args.port), args.url, out_dir, shots))
    finally:
        _stop_browser(proc, profile)


if __name__ == "__main__":
    main()
