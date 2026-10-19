"""ITIL 4 — jelölt módszertani réteg a PMI-gerinc mellett (csak a Xyo projektre).

A PRINCE2-réteg mintájára: saját oldal és fázisonkénti, jelölt blokk,
végig ugyanazzal a jelvénnyel. A tartalom a `content/itil4.yaml`-ban és a `docs/itil4/` alatt él;
a PMI-gerincet és a Xyo-dokumentumokat nem módosítja.

Eltávolítás egy lépésben: ez a fájl, a `content/itil4.yaml`, a `docs/itil4/`, a fázis-YAML-ok
`itil4:` blokkja, az `app.py` „ITIL 4" oldala és a `tests/test_itil4.py`.
"""

from __future__ import annotations

import streamlit as st

from pm_app import config, content, render

GAP_ICON = {"nagy": "🔴", "közepes": "🟡", "kicsi": "🟢"}
GAP_LEGEND = "🔴 nagy hiány · 🟡 közepes · 🟢 kicsi: mennyire hiányzott a Xyo projektből"

TABS = ["Alapok", "Értéklánc", "Gyakorlatok", "Szerepek és igazodás", "Együtt: PMI + PRINCE2 + ITIL", "Mérhető eredmény", "Haladó szint és ITIL 5", "Összefoglaló és minták"]

ACTIVITY_FILL = "#e1e8e4"  # palakék: a szolgáltatás oldala
PHASE_FILL = "#f6e8dd"     # terrakotta árnyalat: a projekt fázisai (pm_app/theme.py)


def load() -> dict:
    return content.load_itil4()


def activity_names(data: dict) -> dict[str, str]:
    return {a["id"]: a["name_hu"] for a in data["value_chain"]["activities"]}


def doc_label(doc_id: str) -> str:
    return content.doc_name(doc_id)


# --------------------------------------------------------------------------- ábra

def _column(title: str, rows: list[tuple[str, str]], fill: str, border: str) -> str:
    """Egy oszlop HTML-táblás csomópontként, soronként egy porttal. A táblán belüli sorrendet a
    graphviz nem rendezi át (külön csomópontoknál a kereszteződések kedvéért összekeverné)."""
    cells = "".join(
        f'<TR><TD PORT="{port}" BGCOLOR="{fill}" COLOR="{border}" STYLE="rounded">{label}</TD></TR>'
        for port, label in rows
    )
    return (
        '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="6" CELLPADDING="7">'
        f'<TR><TD BORDER="0"><B>{title}</B></TD></TR>{cells}</TABLE>>'
    )


def build_value_chain_dot(data: dict) -> str:
    """Az értéklánc hat tevékenysége, és hogy a Xyo fázisai melyikbe esnek."""
    chain = data["value_chain"]
    phases = [(p["id"], f'{p["number"]}. {p["title_hu"]}') for p in content.load_phases()]
    activities = [(a["id"], f'{a["name_hu"]}<BR/><FONT POINT-SIZE="9">{a["name_en"]}</FONT>') for a in chain["activities"]]
    lines = [
        "digraph itil {",
        "  rankdir=LR; nodesep=0.3; ranksep=1.1;",
        '  node [shape=plaintext fontname="Helvetica" fontsize=10];',
        '  edge [color="#8b949e" arrowsize=0.6];',
        f'  phases [label={_column("A Xyo projekt fázisai", phases, PHASE_FILL, "#a14a2c")}];',
        f'  chain [label={_column("Szolgáltatási értéklánc (ITIL 4)", activities, ACTIVITY_FILL, "#4d7280")}];',
        '  igeny [label="Lehetőség\\nvagy igény" shape=note style=filled fillcolor="#f1f3f4"];',
        '  ertek [label="Termékek és\\nszolgáltatások\\n→ érték" shape=note style=filled fillcolor="#e6f4ea"];',
        "  igeny -> chain:engage:w;",
        "  chain:deliver_support:e -> ertek;",
    ]
    for row in chain["phase_map"]["rows"]:
        for activity in row["activities"]:
            lines.append(f'  phases:{row["phase"]}:e -> chain:{activity}:w [style=dashed];')
    lines.append("}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- fülek

def _concept_card(item: dict, name_key: str = "term_hu", en_key: str = "term_en") -> None:
    with st.container(border=True):
        st.markdown(f"**{item[name_key]}** — _{item[en_key]}_")
        st.markdown(item["text"])
        st.markdown(f"**A Xyo-ban:** {item['xyo']}")


def _basics_tab(data: dict) -> None:
    concepts = data["key_concepts"]
    st.subheader("Érték, szolgáltatás, eredmény")
    st.markdown(concepts["intro"])
    for item in concepts["items"]:
        _concept_card(item)

    dims = data["dimensions"]
    st.subheader("A négy dimenzió")
    st.markdown(dims["intro"])
    for item in dims["items"]:
        _concept_card(item, "name_hu", "name_en")
    st.markdown(dims["external"]["intro"])
    render.text_table(
        [{"Tényező": row["factor"], "A Xyo-ban": row["xyo"]} for row in dims["external"]["factors"]]
    )

    svs = data["svs"]
    st.subheader("A Szolgáltatásérték-rendszer (SVS)")
    st.markdown(svs["intro"])
    render.text_table(
        [
            {"Elem": row["name_hu"], "Angolul": row["name_en"], "Mit jelent": row["text"]}
            for row in svs["components"]
        ]
    )

    st.subheader("A hét irányelv")
    st.caption("Minden döntésnél érvényesek. Mindegyiknél: mit jelent, és hogyan jelent meg a Xyo projektben.")
    for number, item in enumerate(data["principles"], start=1):
        with st.container(border=True):
            st.markdown(f"**{number}. {item['name_hu']}** — _{item['name_en']}_")
            st.markdown(item["text"])
            st.markdown(f"**A Xyo-ban:** {item['xyo']}")


def _value_chain_tab(data: dict) -> None:
    chain = data["value_chain"]
    names = activity_names(data)
    st.subheader("A szolgáltatási értéklánc")
    st.markdown(chain["intro"])
    st.graphviz_chart(build_value_chain_dot(data), width="stretch")
    st.caption(
        "Szaggatott nyíl: a Xyo projekt fázisa ehhez a tevékenységhez járul hozzá. A tevékenységek "
        "nem sorrendet jelentenek — az értékáramok fűzik össze őket. Telefonon az ábra kicsi: az "
        "alatta lévő „Hová esik a Xyo projekt?” táblázat ugyanezt mutatja."
    )
    render.text_table(
        [
            {"Tevékenység": a["name_hu"], "Angolul": a["name_en"], "Mit jelent": a["text"], "A Xyo-ban": a["xyo"]}
            for a in chain["activities"]
        ]
    )

    st.subheader("Hová esik a Xyo projekt?")
    st.markdown(chain["phase_map"]["intro"])
    phases = {p["id"]: p for p in content.load_phases()}
    render.text_table(
        [
            {
                "Fázis": f"{phases[row['phase']]['number']}. {phases[row['phase']]['title_hu']}",
                "Értéklánc-tevékenység": ", ".join(names[a] for a in row["activities"]),
                "Miért": row["note"],
            }
            for row in chain["phase_map"]["rows"]
        ]
    )

    streams = data["value_streams"]
    st.subheader("Két értékáram a Xyo üzemeltetéséből")
    st.markdown(streams["intro"])
    for stream in streams["items"]:
        with st.expander(f"**{stream['name']}**"):
            st.markdown(f"**Kiváltó esemény:** {stream['trigger']}  \n**Elvárt eredmény:** {stream['outcome']}")
            st.markdown(f"**Mérőszám:** {stream['metric']}")
            render.text_table(
                [
                    {"Sorszám": i, "Tevékenység": names[step["activity"]], "Lépés": step["step"], "Ki": step["who"]}
                    for i, step in enumerate(stream["steps"], start=1)
                ]
            )
            st.info(stream["lesson"], icon=":material/lightbulb:")


def _practice_card(item: dict, groups: dict) -> None:
    with st.container(border=True):
        st.markdown(f"**{item['name_hu']}** — _{item['name_en']}_ · {groups[item['group']]}")
        st.markdown(f"**Célja:** {item['purpose']}")
        st.markdown(f"**A Xyo-ban:** {item['xyo']}")
        st.markdown(f"{GAP_ICON[item['gap']]} **Mit tenne hozzá:** {item['adds']}")
        st.caption("Kapcsolódó Xyo-dokumentumok: " + " · ".join(doc_label(d) for d in item["docs"]))


def _practices_tab(data: dict) -> None:
    practices = data["practices"]
    groups = practices["groups"]
    st.subheader("A Foundation 15 gyakorlata a Xyo projekten")
    st.markdown(practices["intro"])
    st.caption(GAP_LEGEND)
    foundation = practices["foundation"]
    st.markdown("#### A 7 részletesen ismert gyakorlat")
    for item in (p for p in foundation if p["depth"] == "részletes"):
        _practice_card(item, groups)
    st.markdown("#### A 8 gyakorlat a céljuk szintjén")
    for item in (p for p in foundation if p["depth"] == "cél"):
        _practice_card(item, groups)

    st.info(practices["project_note"], icon=":material/info:")

    st.markdown("#### A többi 19 gyakorlat")
    st.caption("A Foundation-vizsga ezeket nem kéri; a teljes kép kedvéért, csoportonként.")
    render.text_table(
        [
            {"Csoport": groups[row["group"]], "Gyakorlat": row["name_hu"], "Angolul": row["name_en"]}
            for row in sorted(practices["others"], key=lambda r: list(groups).index(r["group"]))
        ]
    )


def _roles_tab(data: dict) -> None:
    roles = data["roles"]
    st.subheader("Kell-e új ember? Ki milyen szerepet visel?")
    st.markdown(roles["intro"])
    render.text_table(
        [
            {"ITIL-szerep": f"{r['role']} ({r['role_en']})", "Ki a Xyo-ban": r["who"], "Mit csinál": r["what"], "Mennyi munka": r["load"]}
            for r in roles["items"]
        ]
    )
    st.warning(roles["concentration"], icon=":material/person_alert:")
    st.info(roles["when_new_people"], icon=":material/groups:")

    expertise = data["expertise"]
    st.subheader("Ki hozza a szakértelmet?")
    st.markdown(expertise["intro"])
    render.text_table([{"Forrás": e["source"], "Ki": e["who"], "Mit ad": e["what"]} for e in expertise["items"]])

    alignment = data["alignment"]
    st.subheader("Kihez és mihez kell igazodni?")
    st.markdown(alignment["intro"])
    for item in alignment["items"]:
        with st.container(border=True):
            st.markdown(f"**{item['who']}**")
            st.markdown(item["why"])

    changes = data["project_changes"]
    st.subheader("Mit változtat a projekten?")
    st.markdown(changes["intro"])
    for number, item in enumerate(changes["items"], start=1):
        st.markdown(f"{number}. **{item['what']}** — {item['detail']}")


def _together_tab(data: dict) -> None:
    together = data["together"]
    st.subheader("PMI + PRINCE2 + ITIL 4: három réteg ugyanazon a munkán")
    st.markdown(together["intro"])
    render.text_table(
        [{"Kérdés": r["question"], "PMI / PMBOK": r["pmi"], "PRINCE2": r["prince2"], "ITIL 4": r["itil"]} for r in together["layers"]]
    )

    st.subheader("Ugyanaz a dolog, három néven")
    query = st.text_input("Keresés", placeholder="pl. change, hypercare, issue", key="itil4-fogalom")
    rows = together["concept_map"]
    if query:
        needle = query.lower()
        rows = [r for r in rows if needle in " ".join(r.values()).lower()]
    render.text_table(
        [{"PMI / PMBOK": r["pmi"], "PRINCE2": r["prince2"], "ITIL 4": r["itil"], "Megjegyzés": r["note"]} for r in rows]
    )

    handover = together["handover_points"]
    st.subheader("Hol ér össze a projekt és a szolgáltatás?")
    st.markdown(handover["intro"])
    render.text_table(
        [{"Mikor": h["when"], "Mit": h["what"], "Ki adja": h["from"], "Ki veszi át": h["to"]} for h in handover["items"]]
    )

    st.subheader("Ahol ütközhetnek — és a feloldás")
    for item in together["conflicts"]:
        with st.container(border=True):
            st.markdown(f"**{item['topic']}**")
            st.markdown(item["resolution"])

    journey = data["error_journey"]
    st.subheader(journey["title"])
    st.markdown(journey["intro"])
    for step in journey["steps"]:
        with st.expander(f"**{step['when']}** — {step['what']}"):
            render.text_table(
                [
                    {"Módszertan": "PMI", "Mit lát": step["pmi"]},
                    {"Módszertan": "PRINCE2", "Mit lát": step["prince2"]},
                    {"Módszertan": "ITIL 4", "Mit lát": step["itil"]},
                ]
            )
    st.markdown("**Mit tanulunk belőle?**")
    for lesson in journey["lessons"]:
        st.markdown(f"- {lesson}")


def _measurable_tab(data: dict) -> None:
    measurable = data["measurable"]
    practice_names = {p["id"]: p["name_hu"] for p in data["practices"]["foundation"]}
    st.subheader("Hozhat-e mérhető eredményt?")
    st.markdown(measurable["intro"])

    st.markdown("#### A Xyo 12 mérőszáma ITIL-szemmel")
    kinds = measurable["kinds"]
    counts = {kind: sum(1 for k in measurable["kpis"] if k["kind"] == kind) for kind in kinds}
    st.caption(" · ".join(f"**{kind}** ({counts[kind]}): {text}" for kind, text in kinds.items()))
    render.text_table(
        [
            {"Kód": k["id"], "Mérőszám": k["name"], "Az érték része": k["kind"], "ITIL-szemmel": k["itil"], "T0": k["t0"], "T+3": k["t3"]}
            for k in measurable["kpis"]
        ]
    )
    st.info(measurable["sla"], icon=":material/handshake:")

    st.markdown("#### Amit eddig nem lehetett mérni")
    st.markdown(measurable["new_metrics_intro"])
    render.text_table(
        [
            {"Mérőszám": m["metric"], "Gyakorlat": practice_names[m["practice"]], "Miért": m["why"], "Honnan lesz adat": m["data"], "Cél": m["target"]}
            for m in measurable["new_metrics"]
        ]
    )
    st.warning(measurable["not_claimed"], icon=":material/rule:")
    st.markdown(measurable["verdict"])


def maturity_average(items: list[dict], key: str) -> float:
    return sum(i[key] for i in items) / len(items)


def _advanced_tab(data: dict) -> None:
    advanced = data["advanced"]
    practice_names = {p["id"]: p["name_hu"] for p in data["practices"]["foundation"]}
    gaps = {p["id"]: p["gap"] for p in data["practices"]["foundation"]}
    st.subheader("A Foundationön túl: a haladó ITIL 4-modulok a Xyo-n")
    st.markdown(advanced["intro"])
    render.text_table(
        [
            {"Modul": f"{m['code']} — {m['name_en']}", "Miről szól": m["focus"], "A Xyo-n": m["xyo"], "Kinek szólna": m["who"]}
            for m in advanced["itil4_modules"]
        ]
    )
    st.markdown("**A címek (designation) és amit kérnek:**")
    for d in advanced["itil4_designations"]:
        st.markdown(f"- **{d['name']}:** Foundation + {', '.join(d['requires'])}. {d['note']}")

    bundles = advanced["practice_bundles"]
    st.markdown("#### A Practice Manager csomagjai — a Foundation 15 gyakorlata")
    st.markdown(bundles["intro"])
    render.text_table(
        [
            {"Csomag": f"{b['code']} — {b['name_en']} ({b['name_hu']})", "Gyakorlatok": ", ".join(practice_names[p] for p in b["practices"]), "A Xyo-ban": b["xyo"]}
            for b in bundles["items"]
        ]
    )

    maturity = advanced["maturity"]
    st.subheader("Mennyire érett ma a Xyo? — önbecslés")
    st.markdown(maturity["intro"])
    st.caption(" · ".join(f"**{s['level']}** — {s['text']}" for s in maturity["scale"]))
    items = maturity["items"]
    st.caption(
        f"Átlag a projekt végén: **{maturity_average(items, 'now'):.1f}** → reális cél 2027-re: "
        f"**{maturity_average(items, 'target'):.1f}** (a {len(items)} gyakorlat átlaga)".replace(".", ",")
    )
    render.text_table(
        [
            {
                "Gyakorlat": practice_names[i["practice"]],
                "Hiány": f"{GAP_ICON[gaps[i['practice']]]} {gaps[i['practice']]}",
                "Most": i["now"],
                "Cél": i["target"],
                "Miért": i["why"],
            }
            for i in items
        ]
    )
    st.info(maturity["ceiling"], icon=":material/stairs:")

    st.subheader("Szabványok: ISO/IEC 20000-1 és 27001")
    render.text_table([{"Mi": s["name"], "Mire való": s["what"], "A Xyo-nál": s["xyo"]} for s in advanced["standards"]])

    itil5 = advanced["itil5"]
    st.subheader("Átvezetés az ITIL 5-re")
    st.markdown(itil5["intro"])
    render.text_table([{"Mi változik": c["topic"], "Röviden": c["what"], "A Xyo-n": c["xyo"]} for c in itil5["changes"]])
    st.markdown("**A tanúsítási rend (ITIL Version 5):**")
    render.text_table([{"Cím vagy modul": r["name"], "Mi kell hozzá": r["requires"]} for r in itil5["scheme"]])
    for fact in itil5["facts"]:
        st.markdown(f"- {fact}")
    st.info(itil5["advice"], icon=":material/school:")
    st.caption("Források: " + " · ".join(itil5["sources"]))

    st.divider()
    st.markdown(advanced["verdict"])


def _show_markdown(text: str) -> None:
    tab_read, tab_src = st.tabs(["Olvasható", "Markdown forrás"])
    with tab_read:
        st.markdown(text)
    with tab_src:
        st.code(text, language="markdown")


def _sample_card(doc: dict, practice_names: dict[str, str]) -> None:
    sample = content.load_sample(doc.get("sample_file"))
    with st.expander(f"**{doc['order']:02d} — {doc['name_hu']}** ({doc['name_en']})"):
        st.markdown(f"**Mire jó?**  \n{doc['why']}")
        st.markdown(f"**Mit tanít:** {doc['teaches']}")
        st.markdown("**Gyakorlatok:** " + ", ".join(practice_names[p] for p in doc["practices"]))
        st.caption("A Xyo-forrásai: " + " · ".join(doc_label(d) for d in doc["sources"]))
        if sample is None:
            st.info("A minta még nem készült el.", icon=":material/hourglass_empty:")
            return
        st.divider()
        left, right = st.columns([2, 1])
        with left:
            show = st.toggle(
                "A minta megjelenítése",
                key=f"show-{doc['id']}",
                help="A minta csak igény szerint töltődik be, hogy az oldal gyors maradjon.",
            )
        with right:
            st.download_button(
                "Letöltés md fájlként",
                data=sample.encode("utf-8"),
                file_name=(config.ROOT / doc["sample_file"]).name,
                mime="text/markdown",
                key=f"dl-{doc['id']}",
                icon=":material/download:",
            )
        if show:
            _show_markdown(sample)


def _summary_tab(data: dict) -> None:
    primer = content.load_sample(data.get("primer_file"))
    if primer:
        st.subheader("Teljes összefoglaló")
        st.caption(data.get("primer_caption", ""))
        st.download_button(
            "Az összefoglaló letöltése (md)",
            data=primer.encode("utf-8"),
            file_name="itil4-osszefoglalo.md",
            mime="text/markdown",
            icon=":material/download:",
            type="primary",
        )
        if st.toggle("Az összefoglaló megjelenítése", key="show-itil4-primer"):
            _show_markdown(primer)
    else:
        st.info("Az összefoglaló még készül.", icon=":material/hourglass_empty:")

    documents = sorted(data.get("documents", []), key=lambda d: d["order"])
    if not documents:
        return
    st.divider()
    st.subheader("ITIL 4 mintadokumentumok — a Xyo projekt adataival")
    st.caption(data.get("documents_caption", ""))
    practice_names = {p["id"]: p["name_hu"] for p in data["practices"]["foundation"]}
    for doc in documents:
        _sample_card(doc, practice_names)


# --------------------------------------------------------------------------- fázisblokk

def phase_block(phase: dict) -> None:
    """A fázis ITIL 4-megfelelője — jelölt, elkülönített kiegészítő réteg."""
    block = phase.get("itil4")
    if not block:
        return
    data = load()
    names = activity_names(data)
    practices = {p["id"]: p for p in data["practices"]["foundation"]}

    st.divider()
    st.subheader(f"{config.BADGE_ITIL4} Módszertani kiegészítés")
    st.caption(config.ITIL4_NOTE)
    with st.expander("Mi ez a fázis ITIL 4 szerint?"):
        st.markdown("**Értéklánc-tevékenység:** " + " · ".join(f"**{names[a]}**" for a in block["activities"]))
        st.markdown(block["summary"])
        foundation = ", ".join(practices[p]["name_hu"] for p in block["practices"])
        others = ", ".join(block.get("other_practices", []))
        st.markdown(f"**Érintett gyakorlatok:** {foundation}" + (f"; a Foundationön túl: {others}" if others else ""))
        st.markdown("**Mit tenne hozzá?**")
        for item in block["adds"]:
            with st.container(border=True):
                st.markdown(f"**{item['what']}**")
                st.caption(item["why"])
        st.caption(f"Érintettek: {block['who']}")
        st.caption("A teljes ITIL 4-réteg, az összefoglaló és a mintadokumentumok az **ITIL 4** oldalon találhatók.")


def view() -> None:
    data = load()
    st.title(f"{config.BADGE_ITIL4} ITIL 4 — módszertani kiegészítés")
    st.markdown(data["intro"])
    with st.expander("Hogyan olvasd ezt az oldalt?"):
        st.markdown(data["how_to_read"])

    tabs = st.tabs(TABS)
    for tab, render_tab in zip(tabs, (_basics_tab, _value_chain_tab, _practices_tab, _roles_tab, _together_tab, _measurable_tab, _advanced_tab, _summary_tab)):
        with tab:
            render_tab(data)

    st.caption(config.ITIL4_TRADEMARK)
