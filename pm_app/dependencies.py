"""Az ütemterv „Függ ettől" oszlopának jelölése: típus és késleltetés.

Jelölés (`docs/2-planning/06-utemterv.md`, „Függőségtípusok, késleltetés, előrehozás"):
jelölés nélkül befejezés–kezdés (BK); `(KK)`, `(BB)`, `(KB)` a többi típus; `+N mn` késleltetés,
`−N mn` előrehozás munkanapban, pl. `1.3 (KK +2 mn)`, `6.4 (BB)`, `5.1 (−14 mn)`.
Az értelmezőt a WBS-nézet és a tesztek is ezt használja, hogy a jelölés egy helyen éljen.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

KIND_NAMES = {
    "BK": "befejezés–kezdés",
    "KK": "kezdés–kezdés",
    "BB": "befejezés–befejezés",
    "KB": "kezdés–befejezés",
}

NOTATION = re.compile(r"\s*\((?P<kind>KK|BB|KB)?\s*(?:(?P<sign>[+−])(?P<lag>\d+) mn)?\)$")


@dataclass(frozen=True)
class Dependency:
    raw: str
    target: str  # az előd azonosítója vagy szövege, jelölés nélkül
    kind: str = "BK"
    lag: int = 0  # munkanap; negatív: előrehozás

    @property
    def kind_name(self) -> str:
        return KIND_NAMES[self.kind]

    def describe(self) -> str:
        """Rövid, olvasható jelölés: „KK +2 mn", „BB", „BK" (jelölés nélküli alapeset)."""
        parts = [self.kind] if self.kind != "BK" or not self.lag else []
        if self.lag:
            parts.append(f"{'+' if self.lag > 0 else '−'}{abs(self.lag)} mn")
        return " ".join(parts) or "BK"


def parse_dependency(raw: str) -> Dependency:
    """Egy függőség; jelölés nélkül (vagy dátumos zárójel esetén) befejezés–kezdés, 0 késleltetéssel."""
    raw = raw.strip()
    m = NOTATION.search(raw)
    if not m or not (m["kind"] or m["lag"]):
        return Dependency(raw, raw)
    lag = int(m["lag"] or 0) * (-1 if m["sign"] == "−" else 1)
    return Dependency(raw, raw[: m.start()].strip(), m["kind"] or "BK", lag)


def parse_dependencies(text: str) -> list[Dependency]:
    """A „Függ ettől" cella összes függősége (`;` vagy `,` választja el)."""
    return [parse_dependency(part) for part in re.split(r"[;,]", text) if part.strip()]
