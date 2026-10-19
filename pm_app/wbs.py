"""WBS-nézet a mintaprojektből — jelölt, kiegészítő nézet.

Az adat forrása három mintadokumentum: a WBS (XYO-CP-103: a lebontás fája és a munkacsomagok
becsült ráfordítása), a WBS-szótár (XYO-CP-104: a kész-definíciók) és az Ütemterv (XYO-CP-106:
dátum, kritikus út, függőségek típussal). Az oldal ezekből rajzol, ezért mindig a dokumentumokkal
egyezik; saját adatot nem tárol. A PMI-gerincet (fázisok, dokumentumok, checklist) nem módosítja.

A dátumokat és a függőségeket a Gantt-nézet olvasója adja (`gantt.load_schedule`), a jelölést a
`dependencies` értelmezi.

Eltávolítás egy lépésben: ez a fájl, az `app.py` „WBS" oldala és a `tests/test_wbs.py`.
"""

from __future__ import annotations

import re

import pandas as pd
import streamlit as st

from pm_app import render
from pm_app.dependencies import parse_dependencies
from pm_app.gantt import (
    CATEGORIES,
    CRITICAL,
    MILESTONE_COLOR,
    NORMAL,
    _first_table,
    _plain,
    _read,
    _section,
    load_schedule,
)

WBS_FILE = "docs/2-planning/03-wbs.md"
DICTIONARY_FILE = "docs/2-planning/04-wbs-szotar.md"

BADGE = ":blue-badge[kiegészítő nézet]"
NOTE = (
    "Ez a nézet a meglévő **WBS**, **WBS-szótár** és **Ütemterv** mintadokumentumból rajzol. "
    "A fázisok, dokumentumok és a checklist tartalmát nem módosítja."
)

# A függőségi fül ezzel nyit: van előde (BK és BB) és utódja is, így a típusok rögtön látszanak.
DEFAULT_PACKAGE = "3.5"

# Egysoros jelmagyarázatok: a jelölés mellett, ott, ahol látszik (nem a lap tetején, amit a lenyitott ág alatt már nem látni).
TREE_LEGEND = (
    ":red[●] kritikus úton van (a csúszása a projekt végét tolja) · a sor: felelős · ráfordítás · "
    "ki végzi · ütem (hó.nap.)"
)
TABLE_LEGEND = "KU = kritikus úton van (✔): a csúszása a projekt végét tolja."
DEPENDENCY_LEGEND = (
    "BK = befejezés–kezdés (alapeset), KK = kezdés–kezdés, BB = befejezés–befejezés, KB = kezdés–befejezés · "
    "+N mn késleltetés (kötelező várakozás), −N mn előrehozás · mn = munkanap"
)

# A 8–80 órás szabály (WBS-dokumentum) kivételei: folyamatos, ütemhez kötött tevékenység.
OVERSIZED = {"1.2"}

_ID = re.compile(r"^\d+(?:\.\d+)*$")
_NODE = re.compile(r"[├└]── (\d+(?:\.\d+)*)\s+(.+)$")


# --------------------------------------------------------------------------- beolvasás

def _tree() -> list[dict]:
    """A lebontás fája: a csomópontok sorrendben, szülővel és szinttel."""
    block = _section(_read(WBS_FILE), "1. A lebontás")
    nodes = []
    for line in block.splitlines():
        m = _NODE.search(line)
        if not m:
            continue
        node_id, name = m.group(1), m.group(2).strip()
        parent = node_id.rsplit(".", 1)[0] if "." in node_id else None
        if "." not in node_id:
            name = name.capitalize()  # a főágak a dokumentumban NAGYBETŰSEK
        nodes.append({"id": node_id, "name": name, "level": node_id.count(".") + 1, "parent": parent})
    return nodes


def _hours(text: str) -> int:
    return int(re.sub(r"\D", "", text.split("óra")[0]))


def _kind(text: str) -> str:
    """„belső", „külső", „vegyes"; a „belső + szállító" és a „belső (kész)" belső."""
    return "vegyes" if text.startswith("vegyes") else "külső" if text.startswith("külső") else "belső"


def _package_rows() -> dict[str, dict]:
    text = _read(WBS_FILE)
    rows = {}
    for row in _first_table(_section(text, "2. Munkacsomagok becsült ráfordítással")):
        if not _ID.match(row[0]):
            continue  # az „Összesen" sor
        rows[row[0]] = {
            "short": _plain(row[1]),
            "owner": _plain(row[2]),
            "hours": _hours(row[3]),
            "kind": _kind(row[4]),
            "kind_text": _plain(row[4]),
        }
    # A vegyes csomagok megosztása a táblázat alatti lábjegyzetben: „3.3.1: 24 + 24, 3.4.2: 12 + 12 …"
    split = {
        pid: (int(a), int(b))
        for pid, a, b in re.findall(r"(\d\.\d(?:\.\d)?): (\d+) \+ (\d+)", _section(text, "2. Munkacsomagok"))
    }
    for pid, row in rows.items():
        internal, external = split.get(pid, (row["hours"], 0) if row["kind"] == "belső" else (0, row["hours"]))
        row["internal"], row["external"] = internal, external
    return rows


def _dictionary() -> dict[str, dict]:
    """A WBS-szótár lapjai: {"2.3.1": {"Felelős": ..., "Kész-definíció": ..., "title": ...}}."""
    text = _read(DICTIONARY_FILE)
    entries = {}
    for m in re.finditer(r"^## (\d+(?:\.\d+)*) — (.+)$", text, flags=re.MULTILINE):
        body = _section(text, m.group(0).lstrip("# "))
        fields = {row[0].strip("*"): row[1] for row in _first_table(body) if len(row) == 2}
        entries[m.group(1)] = {"title": m.group(2).strip(), **fields}
    return entries


@st.cache_data(show_spinner=False)
def load() -> dict:
    """Ágak, csomópontok és munkacsomagok az ütemtervvel és a szótárral összekapcsolva."""
    nodes = _tree()
    by_id = {n["id"]: n for n in nodes}
    parents = {n["parent"] for n in nodes}
    rows = _package_rows()
    dictionary = _dictionary()
    schedule = load_schedule()
    scheduled = {t["wbs"]: t for t in schedule["tasks"] if t["wbs"]}

    packages = []
    for node in nodes:
        if node["id"] in parents:
            continue
        row = rows[node["id"]]
        task = scheduled.get(node["id"])
        packages.append(
            {
                "id": node["id"],
                "name": node["name"],
                "branch": node["id"].split(".")[0],
                "parent": node["parent"],
                "owner": row["owner"],
                "hours": row["hours"],
                "internal": row["internal"],
                "external": row["external"],
                "kind": row["kind"],
                "kind_text": row["kind_text"],
                "start": task["start"] if task else None,
                "end": task["end"] if task else None,
                "critical": task["critical"] if task else False,
                "deps": task["deps"] if task else "",
                "scheduled": task is not None,
                "dictionary": dictionary.get(node["id"]),
            }
        )

    branches = []
    for node in (n for n in nodes if n["level"] == 1):
        own = [p for p in packages if p["branch"] == node["id"]]
        dates = [p["start"] for p in own if p["start"]] + [p["end"] for p in own if p["end"]]
        branches.append(
            {
                "id": node["id"],
                "name": node["name"],
                "count": len(own),
                "hours": sum(p["hours"] for p in own),
                "internal": sum(p["internal"] for p in own),
                "external": sum(p["external"] for p in own),
                "start": min(dates) if dates else None,
                "end": max(dates) if dates else None,
            }
        )
    return {
        "nodes": nodes,
        "by_id": by_id,
        "packages": packages,
        "branches": branches,
        "schedule": schedule,
        "milestones": {m["key"]: m for m in schedule["milestones"]},
        "own_rows": [t for t in schedule["tasks"] if not t["wbs"]],
    }


# --------------------------------------------------------------------------- függőségek

def resolve(target: str, data: dict) -> dict:
    """Egy függőség célja: munkacsomag, csoport (`2.1.x`), mérföldkő, az ütemterv saját sora
    (várakozás, ablak) vagy külső esemény (határidő, szállítás)."""
    by_id = data["by_id"]
    packages = {p["id"] for p in data["packages"]}
    if target in packages:
        return {"type": "package", "ids": [target], "label": f"{target} {by_id[target]['name']}"}
    if target.endswith(".x") and target[:-2] in by_id:
        ids = [p["id"] for p in data["packages"] if p["id"].startswith(target[:-1])]
        return {"type": "group", "ids": ids, "label": f"{target[:-2]} {by_id[target[:-2]]['name']} ({', '.join(ids)})"}
    if target in data["milestones"]:
        m = data["milestones"][target]
        return {"type": "milestone", "ids": [], "label": f"{target} {m['name']} ({m['date']:%m.%d.})"}
    for row in data["own_rows"]:
        if target.lower() in row["name"].lower():
            return {"type": "row", "ids": [], "label": row["name"]}
    return {"type": "external", "ids": [], "label": target}


def predecessors(package: dict, data: dict) -> list[dict]:
    """Mitől függ a csomag (az ütemterv szerint), típussal és késleltetéssel."""
    result = []
    for dep in parse_dependencies(package["deps"]):
        result.append({"dependency": dep, **resolve(dep.target, data)})
    return result


def successors(package_id: str, data: dict) -> list[dict]:
    """Mi függ a csomagtól: azok a csomagok, amelyek függőségei (akár `.x` csoporton át) ide mutatnak."""
    result = []
    for other in data["packages"]:
        for dep in parse_dependencies(other["deps"]):
            if package_id in resolve(dep.target, data)["ids"]:
                result.append({"dependency": dep, "package": other})
    return result


def edges(data: dict) -> list[tuple[str, str, str]]:
    """A munkacsomagok közti élek: (előd, utód, jelölés), csoportokat kibontva."""
    found = []
    for pkg in data["packages"]:
        for dep in parse_dependencies(pkg["deps"]):
            for pred in resolve(dep.target, data)["ids"]:
                found.append((pred, pkg["id"], dep.describe()))
    return found


def build_dot(data: dict) -> str:
    """A csomagok függőségi hálója, ágankénti csoportokkal; a kritikus úton lévők piros szegéllyel."""
    palette = ["#e8f0fe", "#e6f4ea", "#fef7e0", "#fce8e6", "#f3e8fd", "#e0f7fa", "#f1f3f4", "#fff0e0"]
    used = {pid for a, b, _ in edges(data) for pid in (a, b)}
    lines = [
        "digraph wbs {",
        "  rankdir=LR;",
        "  nodesep=0.2; ranksep=0.5;",
        '  node [shape=box style="rounded,filled" fontname="Helvetica" fontsize=10];',
        '  edge [color="#8b949e" arrowsize=0.6 fontname="Helvetica" fontsize=9];',
    ]
    for i, branch in enumerate(data["branches"]):
        members = [p for p in data["packages"] if p["branch"] == branch["id"] and p["id"] in used]
        if not members:
            continue
        lines.append(f"  subgraph cluster_{branch['id']} {{")
        lines.append(f'    label="{branch["id"]} {branch["name"]}"; style="rounded"; color="#c9d1d9"; fontsize=11;')
        for pkg in members:
            border = CATEGORIES[CRITICAL] if pkg["critical"] else "#9aa0a6"
            label = f"{pkg['id']}\\n{_wrap(pkg['name'])}"
            lines.append(f'    "{pkg["id"]}" [label="{label}" fillcolor="{palette[i % len(palette)]}" color="{border}"];')
        lines.append("  }")
    for pred, succ, note in sorted(set(edges(data))):
        attr = f' [label="{note}"]' if note != "BK" else ""
        lines.append(f'  "{pred}" -> "{succ}"{attr};')
    lines.append("}")
    return "\n".join(lines)


def _wrap(text: str, width: int = 22) -> str:
    words, lines, current = text.split(), [], ""
    for word in words:
        if current and len(current) + 1 + len(word) > width:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    lines.append(current)
    return "\\n".join(lines)


# --------------------------------------------------------------------------- megjelenítés

def _hu(number: int) -> str:
    """Ezres tagolás nem törő szóközzel, mint a dokumentumokban („1 260")."""
    return f"{number:,}".replace(",", "\u00a0")


def _span(pkg: dict) -> str:
    if not pkg["scheduled"]:
        return "nincs külön ütemezve"
    return f"{pkg['start']:%m.%d.}–{pkg['end']:%m.%d.}"


def _branch_summary(branch: dict) -> str:
    span = f", {branch['start']:%m.%d.}–{branch['end']:%m.%d.}" if branch["start"] else ""
    return f"{branch['id']}. {branch['name']} — {branch['count']} munkacsomag, {_hu(branch['hours'])} óra{span}"


def _tree_markdown(branch: dict, data: dict) -> str:
    """Egy ág lebontása beágyazott felsorolásként (mobilon is olvasható, nem szöveges ábra)."""
    lines = []
    for node in data["nodes"]:
        if node["level"] == 1 or not node["id"].startswith(branch["id"] + "."):
            continue
        indent = "    " * (node["level"] - 2)
        pkg = next((p for p in data["packages"] if p["id"] == node["id"]), None)
        if pkg is None:
            lines.append(f"{indent}- **{node['id']}** {node['name']}")
            continue
        flag = " :red[●]" if pkg["critical"] else ""
        lines.append(f"{indent}- **{pkg['id']}** {pkg['name']}{flag}  \n"
                     f"{indent}  {pkg['owner']} · {pkg['hours']} óra · {pkg['kind']} · {_span(pkg)}")
    return "\n".join(lines)


def _package_label(pkg: dict) -> str:
    return f"{pkg['id']}  {pkg['name']}"


def _tree_tab(data: dict) -> None:
    st.caption("A főágak lenyithatók.")
    for branch in data["branches"]:
        with st.expander(_branch_summary(branch)):
            st.markdown(TREE_LEGEND)  # nem caption: a halványított felirat elvenné a pont pirosát
            st.markdown(_tree_markdown(branch, data))


def _table_tab(data: dict) -> None:
    packages = data["packages"]
    controls = st.columns([2, 2, 2])
    with controls[0]:
        branch = st.selectbox(
            "Ág", ["Mind"] + [f"{b['id']}. {b['name']}" for b in data["branches"]], key="wbs-ag"
        )
    with controls[1]:
        kind = st.selectbox("Ki végzi?", ["Mind", "belső", "külső", "vegyes"], key="wbs-kind")
    with controls[2]:
        critical_only = st.toggle("Csak a kritikus úton", key="wbs-ku")

    shown = [
        p for p in packages
        if (branch == "Mind" or p["branch"] == branch.split(".")[0])
        and (kind == "Mind" or p["kind"] == kind)
        and (not critical_only or p["critical"])
    ]
    st.caption(f"{len(shown)} munkacsomag, összesen {_hu(sum(p['hours'] for p in shown))} óra · {TABLE_LEGEND}")
    render.text_table(
        [
            {
                "WBS": p["id"],
                "Munkacsomag": p["name"],
                "Felelős": p["owner"],
                "Óra": p["hours"],
                "Ütem": _span(p),
                "KU": "✔" if p["critical"] else "",
            }
            for p in shown
        ],
        height=480,
    )


def _dependencies_tab(data: dict) -> None:
    packages = data["packages"]
    chosen = st.selectbox(
        "Munkacsomag", [p["id"] for p in packages],
        format_func=lambda pid: _package_label(next(p for p in packages if p["id"] == pid)),
        index=[p["id"] for p in packages].index(DEFAULT_PACKAGE),
        key="wbs-csomag",
    )
    pkg = next(p for p in packages if p["id"] == chosen)
    st.markdown(f"#### {_package_label(pkg)}")
    st.caption(
        f"{pkg['owner']} · {pkg['hours']} óra ({pkg['kind']}) · {_span(pkg)}"
        + (" · kritikus úton" if pkg["critical"] else "")
    )

    left, right = st.columns(2)
    with left:
        st.markdown("**Mitől függ?**")
        pred = predecessors(pkg, data)
        if pred:
            render.text_table(
                [{"Előd": p["label"], "Típus": f"{p['dependency'].kind_name} ({p['dependency'].describe()})"}
                 for p in pred]
            )
        elif pkg["scheduled"]:
            st.caption("Nincs előde: a projekt indulásától fogva indulhat.")
        else:
            st.caption("Az ütemterv nem tartalmaz külön sort ehhez a csomaghoz; lásd a szótári lapot alább.")
    with right:
        st.markdown("**Mi függ tőle?**")
        succ = successors(pkg["id"], data)
        if succ:
            render.text_table(
                [{"Utód": _package_label(s["package"]),
                  "Típus": f"{s['dependency'].kind_name} ({s['dependency'].describe()})"}
                 for s in succ]
            )
        else:
            st.caption("Egy másik munkacsomag sem épít közvetlenül erre.")

    st.caption(DEPENDENCY_LEGEND)

    entry = pkg["dictionary"]
    if entry:
        with st.expander("WBS-szótár: a csomag teljes lapja", expanded=False):
            for field in ("Felelős", "Mit tartalmaz", "Mit NEM tartalmaz", "Kész-definíció",
                          "Becsült ráfordítás", "Függőség", "Kockázat"):
                if field in entry:
                    st.markdown(f"**{field}.** {entry[field]}")
    else:
        st.caption("Ehhez a csomaghoz nincs külön szótári lap a mintában (csak a kritikus és a vitás csomagoké van).")

    st.divider()
    if st.toggle(
        "A teljes függőségháló",
        key="wbs-halo",
        help="Az összes munkacsomag egyben. Szélesebb képernyőre való; telefonon a fenti, csomagonkénti nézet olvashatóbb.",
    ):
        st.graphviz_chart(build_dot(data), width="stretch")
        st.caption("A piros szegély a kritikus úton lévő munkacsomag. Az élfelirat a nem alapértelmezett "
                   "függőségtípust és a késleltetést mutatja (pl. KK +2 mn).")


def _effort_tab(data: dict) -> None:
    packages = data["packages"]
    total = sum(p["hours"] for p in packages)
    internal = sum(p["internal"] for p in packages)
    external = sum(p["external"] for p in packages)
    cols = st.columns(4)
    cols[0].metric("Munkacsomag", len(packages))
    cols[1].metric("Összes ráfordítás", f"{_hu(total)} óra")
    cols[2].metric("Belső", f"{_hu(internal)} óra")
    cols[3].metric("Külső (szállító)", f"{_hu(external)} óra")

    frame = pd.DataFrame(
        [{"Ág": f"{b['id']}. {b['name']}", "Belső": b["internal"], "Külső": b["external"]} for b in data["branches"]]
    ).set_index("Ág")
    st.bar_chart(frame, horizontal=True, stack=True, color=[CATEGORIES[NORMAL], MILESTONE_COLOR], height=320)
    st.caption(
        "A vegyes munkacsomagok (3.3.1, 3.4.2, 3.5, 5.2) órái a WBS-dokumentum lábjegyzete szerint oszlanak "
        "meg belső és külső között."
    )
    big = [p for p in packages if p["id"] in OVERSIZED]
    if big:
        st.info(
            "A munkacsomag szabály szerint 8–80 óra. Kivétel: "
            + ", ".join(f"**{p['id']} {p['name']}** ({p['hours']} óra)" for p in big)
            + " — folyamatos, ütemhez kötött tevékenység, amelynek nincs kézzelfogható köztes eredménye.",
            icon=":material/info:",
        )


def view() -> None:
    st.title(f"WBS {BADGE}")
    st.caption("Xyo Cloud Pilot — munkalebontási szerkezet, befagyasztva 2026.03.13-án")
    st.info(NOTE, icon=":material/info:")

    data = load()
    tab_tree, tab_table, tab_deps, tab_effort = st.tabs(["Fa", "Táblázat", "Függőségek", "Ráfordítás"])
    with tab_tree:
        _tree_tab(data)
    with tab_table:
        _table_tab(data)
    with tab_deps:
        _dependencies_tab(data)
    with tab_effort:
        _effort_tab(data)
