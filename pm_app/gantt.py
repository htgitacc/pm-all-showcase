"""Gantt-nézet a mintaprojekt ütemtervéből — jelölt, kiegészítő nézet.

Az adat egyetlen forrása az Ütemterv mintadokumentum (XYO-CP-106), a tény-
dátumoké és a tartalékfelhasználásé a Mérföldkő-riport (XYO-CP-308): a diagram
ezekből rajzol, ezért mindig a dokumentumokkal egyezik. A PMI-gerincet (fázisok,
dokumentumok, checklist) nem módosítja.

Eltávolítás egy lépésben: ez a fájl, az `app.py` „Gantt-nézet" oldala és a
`tests/test_gantt.py`.
"""

from __future__ import annotations

import datetime as dt
import re

import altair as alt
import pandas as pd
import streamlit as st

from pm_app import config

SCHEDULE_FILE = "docs/2-planning/06-utemterv.md"
WBS_FILE = "docs/2-planning/03-wbs.md"
MILESTONE_REPORT_FILE = "docs/4-monitoring/08-merfoldko-riport.md"

BADGE = ":blue-badge[kiegészítő nézet]"
NOTE = (
    "Ez a nézet a meglévő **Ütemterv** mintadokumentumból rajzol, és a "
    "**Mérföldkő-riport** tény-dátumait teszi mellé. A fázisok, dokumentumok és "
    "a checklist tartalmát nem módosítja."
)

# A sávok kategóriái és színei — a sorrend a jelmagyarázaté is.
CRITICAL = "Kritikus út"
CRITICAL_WAIT = "Kritikus út — várakozás"
NORMAL = "Nem kritikus"
NORMAL_WAIT = "Nem kritikus — várakozás"
BUFFER = "Jelölt tartalék"
CATEGORIES = {
    CRITICAL: "#d1453b",
    CRITICAL_WAIT: "#eda39c",
    NORMAL: "#4f7fc9",
    NORMAL_WAIT: "#a9c0e6",
    BUFFER: "#3f9e8a",
}
MILESTONE_COLOR = "#e0a030"
HOLIDAY_COLOR = "#9aa0a6"


# --------------------------------------------------------------------------- beolvasás

def _read(rel_path: str) -> str:
    return (config.ROOT / rel_path).read_text(encoding="utf-8")


def _section(text: str, heading_start: str) -> str:
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
    raise ValueError(f"Nincs ilyen szakasz: {heading_start!r}")


def _first_table(text: str) -> list[list[str]]:
    """A szakasz első markdown-táblájának sorai, fejléc és elválasztó nélkül."""
    rows = []
    for line in text.splitlines():
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
        elif rows:
            break
    return rows[2:]


def _plain(text: str) -> str:
    return text.replace("**", "").strip()


def _full_date(text: str) -> dt.date | None:
    match = re.search(r"(\d{4})\.(\d\d)\.(\d\d)\.", text)
    return dt.date(*map(int, match.groups())) if match else None


def _short_date(text: str, year: int) -> dt.date:
    month, day = re.search(r"(\d\d)\.(\d\d)\.", text).groups()
    return dt.date(year, int(month), int(day))


def _days(text: str) -> int:
    return int(re.search(r"\d+", _plain(text)).group(0))


def wbs_areas() -> dict[str, str]:
    """A WBS főágai sorrendben: {"1": "Projektirányítás", ...}."""
    found = re.findall(r"[├└]── (\d)  ([A-ZÁÉÍÓÖŐÚÜŰ ]+)", _read(WBS_FILE))
    return {number: name.strip().capitalize() for number, name in found}


@st.cache_data(show_spinner=False)
def load_schedule() -> dict:
    """Az ütemterv feladatai, mérföldkövei, tartalékai és munkaszüneti napjai, a tényekkel."""
    text = _read(SCHEDULE_FILE)
    report = _read(MILESTONE_REPORT_FILE)

    actual = {row[0]: _full_date(row[3]) for row in _first_table(_section(report, "1. Mérföldkövek"))}
    milestones = [
        {
            "key": row[0],
            "name": row[1],
            "date": _full_date(row[2]),
            "critical": row[3] == "✔",
            "actual": actual.get(row[0]),
        }
        for row in _first_table(_section(text, "1. Mérföldkövek"))
    ]
    year = milestones[0]["date"].year

    buffers = [
        {"name": _plain(row[0]), "planned": _days(row[1])}
        for row in _first_table(_section(text, "5. Hol van a tartalékidő?"))
        if not row[0].startswith("**")
    ]
    used = {_plain(row[0]): _days(row[2]) for row in _first_table(_section(report, "3. Ahol tartalékidőt"))}
    for buffer in buffers:
        buffer["used"] = used.get(buffer["name"])

    areas = wbs_areas()
    tasks, area = [], ""
    for order, row in enumerate(_first_table(_section(text, "2. Ütemterv munkacsomagonként"))):
        wbs = row[0]
        own_row = wbs == "—"  # nem WBS-munkacsomag: várakozás (ajánlat, jóváhagyás, szállítás) vagy ablak
        if not own_row:
            area = areas.get(wbs.split(".")[0], "")
        # A WBS nélküli sor a megelőző munkacsomag ágához tartozik (pl. a szállítás a beszerzéshez).
        name = _plain(row[1])
        short = name.split(" (")[0]
        is_buffer = own_row and any(b["name"].startswith(short) for b in buffers)
        tasks.append(
            {
                "order": order,
                "wbs": "" if own_row else wbs,
                "name": name,
                "label": name if own_row else f"{wbs}  {name}",
                "area": area,
                "start": _short_date(row[2], year),
                "end": _short_date(row[3], year),
                "days": int(row[4]),
                "deps": row[5],
                "critical": row[6] == "✔",
                "waiting": own_row and not is_buffer,
                "buffer": is_buffer,
            }
        )

    # A két hullám közti rés nem sor a táblában, de jelölt tartalék: a diagramon is látszódjon.
    by_wbs = {t["wbs"]: t for t in tasks if t["wbs"]}
    for buffer in buffers:
        gap = re.match(r"A (\d+\.\d+) és (\d+\.\d+) hullám között", buffer["name"])
        if gap and gap.group(1) in by_wbs and gap.group(2) in by_wbs:
            before, after = by_wbs[gap.group(1)], by_wbs[gap.group(2)]
            start, end = before["end"] + dt.timedelta(days=1), after["start"] - dt.timedelta(days=1)
            tasks.append(
                {
                    "order": before["order"] + 0.5,
                    "wbs": "",
                    "name": f"Tartalék a {gap.group(1)} és {gap.group(2)} hullám között",
                    "label": f"Tartalék a {gap.group(1)} és {gap.group(2)} hullám között",
                    "area": before["area"],
                    "start": start,
                    "end": end,
                    "days": (end - start).days + 1,
                    "deps": gap.group(1),
                    "critical": before["critical"] and after["critical"],
                    "waiting": False,
                    "buffer": True,
                }
            )

    note = next(p for p in text.split("\n\n") if "Munkaszüneti napok" in p)
    holidays = [
        {"date": _short_date(day, year), "name": (name or "munkaszüneti nap").strip()}
        for day, name in re.findall(r"(\d\d\.\d\d\.)(?:\s*\(([^)]+)\))?", note)
    ]
    return {"tasks": tasks, "milestones": milestones, "buffers": buffers, "holidays": holidays}


def category(task: dict) -> str:
    if task["buffer"]:
        return BUFFER
    if task["critical"]:
        return CRITICAL_WAIT if task["waiting"] else CRITICAL
    return NORMAL_WAIT if task["waiting"] else NORMAL


def _milestone_label(m: dict) -> str:
    return f"{m['key']}  {m['name']}"


def row_order(tasks: list[dict], milestones: list[dict], by_wbs: bool) -> list[str]:
    """A sorok sorrendje: időrendben (mérföldkövekkel együtt), vagy WBS-áganként."""
    if by_wbs:
        rank = {name: i for i, name in enumerate(wbs_areas().values())}

        def key(t):
            parts = tuple(int(p) for p in t["wbs"].split(".")) if t["wbs"] else (99,)
            return rank.get(t["area"], 99), parts, t["order"]

        return [_milestone_label(m) for m in milestones] + [t["label"] for t in sorted(tasks, key=key)]
    entries = [(t["start"], 1, t["end"], t["label"]) for t in tasks]
    entries += [(m["date"], 0, m["date"], _milestone_label(m)) for m in milestones]
    return [label for *_, label in sorted(entries)]


# ----------------------------------------------------------------------------- diagram

def build_chart(data: dict, critical_only: bool = False, include_measurement: bool = False,
                by_wbs: bool = False) -> alt.LayerChart:
    project_end = max(t["end"] for t in data["tasks"])
    tasks = [t for t in data["tasks"] if t["critical"] or not critical_only]
    milestones = [
        m for m in data["milestones"]
        if (include_measurement or m["date"] <= project_end) and (m["critical"] or not critical_only)
    ]
    ordered = row_order(tasks, milestones, by_wbs)

    bars = pd.DataFrame(
        [
            {
                "Sor": t["label"],
                "Kezdés": pd.Timestamp(t["start"]),
                "Vége": pd.Timestamp(t["end"] + dt.timedelta(days=1)),  # a befejezés napja is a sávban van
                "Befejezés": pd.Timestamp(t["end"]),
                "Kategória": category(t),
                "Kritikus úton": "igen" if t["critical"] else "nem",
                "WBS-ág": t["area"],
                "Naptári nap": t["days"],
                "Függ ettől": t["deps"],
            }
            for t in tasks
        ]
    )
    points = pd.DataFrame(
        [
            {
                "Sor": _milestone_label(m),
                "Dátum": pd.Timestamp(m["date"]),
                "Tény": f"{m['actual']:%Y.%m.%d.}" if m["actual"] else "még nem teljesült",
                "Kritikus úton": "igen" if m["critical"] else "nem",
            }
            for m in milestones
        ]
    )

    first = min([t["start"] for t in tasks] + [m["date"] for m in milestones])
    last = max([t["end"] for t in tasks] + [m["date"] for m in milestones])
    holidays = pd.DataFrame(
        [
            {
                "Kezdés": pd.Timestamp(h["date"]),
                "Vége": pd.Timestamp(h["date"] + dt.timedelta(days=1)),
                "Munkaszüneti nap": f"{h['date']:%m.%d.} — {h['name']}",
            }
            for h in data["holidays"]
            if first <= h["date"] <= last
        ],
        columns=["Kezdés", "Vége", "Munkaszüneti nap"],
    )

    x_scale = alt.Scale(domain=[pd.Timestamp(first - dt.timedelta(days=2)), pd.Timestamp(last + dt.timedelta(days=3))])
    x_axis = alt.Axis(format="%m.%d.", tickCount="week", title=None, labelAngle=0, grid=True, orient="top")
    y = alt.Y("Sor:N", sort=ordered, title=None, axis=alt.Axis(labelLimit=340))

    holiday_layer = alt.Chart(holidays).mark_rect(color=HOLIDAY_COLOR, opacity=0.35).encode(
        x=alt.X("Kezdés:T", scale=x_scale, axis=x_axis),
        x2="Vége:T",
        tooltip=["Munkaszüneti nap:N"],
    )
    bar_layer = alt.Chart(bars).mark_bar(cornerRadius=2, height={"band": 0.7}).encode(
        x=alt.X("Kezdés:T", scale=x_scale, axis=x_axis),
        x2="Vége:T",
        y=y,
        color=alt.Color(
            "Kategória:N",
            scale=alt.Scale(domain=list(CATEGORIES), range=list(CATEGORIES.values())),
            legend=alt.Legend(orient="top", title=None, columns=2, labelLimit=0),
        ),
        tooltip=[
            alt.Tooltip("Sor:N", title="Feladat"),
            "WBS-ág:N",
            alt.Tooltip("Kezdés:T", format="%Y.%m.%d."),
            alt.Tooltip("Befejezés:T", format="%Y.%m.%d."),
            "Naptári nap:Q",
            "Függ ettől:N",
            "Kategória:N",
            "Kritikus úton:N",
        ],
    )
    milestone_layer = alt.Chart(points).mark_point(
        shape="diamond", size=170, filled=True, color=MILESTONE_COLOR, opacity=1
    ).encode(
        x=alt.X("Dátum:T", scale=x_scale, axis=x_axis),
        y=y,
        tooltip=[
            alt.Tooltip("Sor:N", title="Mérföldkő"),
            alt.Tooltip("Dátum:T", title="Terv", format="%Y.%m.%d."),
            "Tény:N",
            "Kritikus úton:N",
        ],
    )
    # Szándékosan nem nagyítható: a görgő a magas diagram fölött is a lapot görgesse.
    return alt.layer(holiday_layer, bar_layer, milestone_layer).properties(height=24 * len(ordered) + 40)


# -------------------------------------------------------------------------------- oldal

LESSON = """
**Miért kell?** A Gantt-diagram egy pillantásra megmutatja, mi fut párhuzamosan,
mi mire vár, és hol nincs mozgástér. A Steering Committee-nek ez a leggyorsabban
érthető ütemkép — egy 40 soros táblázatot senki nem olvas végig egy ülésen.

**Hogyan olvasd?**
- **Piros = kritikus út.** Ha bármelyik piros sáv csúszik, a projekt vége csúszik.
  M5 előtt **két piros ág** fut párhuzamosan (Entra ID → Intune → Autopilot,
  illetve SharePoint → visszaállítási teszt): bármelyik késése elég a csúszáshoz.
- **Halvány sáv = várakozás.** Az ajánlati szakasz, a belső jóváhagyás és a
  hardverszállítás nem a csapat munkája, de ugyanúgy telik a naptár. A beszerzés
  33 naptári napjából csak kb. 9 munkanap a tényleges munka.
- **Kék = van tartalék.** A hardverszállítás például 2 munkanappal a 2. hullám
  előtt ér véget — ezért nem kritikus, de hetente figyelni kell.
- **Zöld = jelölt tartalék.** A 9 napos hibajavítási ablak és a 7.2–7.3 hullám
  közti rés. Ez a projekt teljes időtartaléka, és látható helyen van.
- **Szürke sáv = munkaszüneti nap.** Határidő és bontás nem eshet rá.

**Tipikus hibák**
- **A Gantt nem a terv, csak a képe.** Függőségek nélkül csak színes csíkok: a
  kritikus utat a függőségekből kell kiszámolni, nem ránézésre kiszínezni.
- **A várakozást kihagyják.** Az ajánlati határidő és a jóváhagyási kör nem
  „feladat", ezért kimarad a tervből — és utólag derül ki, hogy elment egy hónap.
- **A tartalékot a feladatokba rejtik.** „Mindenhova +20%" — így senki nem tudja
  megmondani, mennyi tartalék maradt. Itt külön sávként látszik, és a
  Mérföldkő-riport méri, mennyi fogyott el belőle.
- **A baseline-t felülírják.** A jóváhagyott ütemtervet befagyasztod; a tény
  mellé kerül (lent), nem a helyére. Különben soha nem tudod megmutatni, mennyit
  csúsztál és miért.
"""


def view() -> None:
    st.title(f"Gantt-nézet {BADGE}")
    st.caption("Xyo Cloud Pilot — baseline ütemterv, befagyasztva 2026.03.13-án")
    st.info(NOTE, icon=":material/info:")

    data = load_schedule()
    tasks, milestones, buffers = data["tasks"], data["milestones"], data["buffers"]

    controls = st.columns([2, 2, 3])
    with controls[0]:
        scope = st.segmented_control(
            "Mit mutasson?", ["Teljes ütemterv", "Csak a kritikus út"], default="Teljes ütemterv"
        )
    with controls[1]:
        order = st.segmented_control("Sorrend", ["Időrendben", "WBS szerint"], default="Időrendben")
    with controls[2]:
        include_measurement = st.toggle(
            "A mérési szakasz is (M11 — PIR)",
            help="A PIR három hónappal a projektzárás után van; bekapcsolva az időtengely októberig nyúlik.",
        )

    st.altair_chart(
        build_chart(
            data,
            critical_only=scope == "Csak a kritikus út",
            include_measurement=include_measurement,
            by_wbs=order == "WBS szerint",
        ),
        width="stretch",
    )
    st.caption(
        "A ◆ mérföldkő, a szürke sáv munkaszüneti nap. A sávra mutatva a függőségeket is "
        "látod; a diagram jobb felső sarkában teljes képernyőre nagyíthatod."
    )

    by_key = {m["key"]: m for m in milestones}
    done = [m for m in milestones if m["actual"]]
    on_time = [m for m in done if m["actual"] <= m["date"]]
    planned = sum(b["planned"] for b in buffers)
    used = sum(b["used"] or 0 for b in buffers)
    metrics = st.columns(4)
    metrics[0].metric(
        "Baseline → projektzárás",
        f"{(by_key['M10']['date'] - by_key['M3']['date']).days} nap",
        help="Naptári napok az M3 (baseline) és az M10 (projekt lezárva) között.",
    )
    metrics[1].metric("Kritikus úton lévő sor", f"{sum(t['critical'] for t in tasks)} / {len(tasks)}")
    metrics[2].metric(
        "Jelölt tartalék",
        f"{planned} nap",
        delta=f"{used} nap felhasználva",
        delta_color="off",
        help="Az ütemterv 5. pontja szerint; a felhasználás a Mérföldkő-riportból.",
    )
    metrics[3].metric(
        "Mérföldkő határidőre",
        f"{len(on_time)} / {len(done)}",
        help="A Mérföldkő-riport tény-dátumai alapján, a még nem teljesültek nélkül.",
    )

    with st.expander("Hogyan olvasd a Gantt-diagramot — és mit ne higgy el neki", icon=":material/school:"):
        st.markdown(LESSON)

    st.subheader("Mérföldkövek — terv és tény")
    st.dataframe(
        [
            {
                "#": m["key"],
                "Mérföldkő": m["name"],
                "Terv": f"{m['date']:%Y.%m.%d.}",
                "Tény": f"{m['actual']:%Y.%m.%d.}" if m["actual"] else "—",
                "Eltérés (nap)": (m["actual"] - m["date"]).days if m["actual"] else None,
                "Kritikus úton": "✔" if m["critical"] else "",
            }
            for m in milestones
        ],
        hide_index=True,
        width="stretch",
    )
    st.caption(
        "Forrás: *Ütemterv és mérföldkőlista* (XYO-CP-106, 2. fázis) és *Mérföldkő-riport* "
        "(XYO-CP-308, 4. fázis). A diagram ezekből a dokumentumokból készül, ezért mindig "
        "velük egyezik."
    )
