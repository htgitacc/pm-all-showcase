"""Az egyes oldalak megjelenítése."""

from __future__ import annotations

import functools

import streamlit as st

from pm_app import config, content, downloads, progress, render


# --------------------------------------------------------------------------- áttekintés

def overview() -> None:
    meta = content.load_meta()
    st.title(config.APP_TITLE)
    st.caption(config.APP_SUBTITLE)

    st.markdown(meta.get("intro", ""))

    st.progress(
        progress.overall_ratio(),
        text=f"Teljes haladás a kötelező lépéseken: {progress.overall_ratio():.0%}",
    )

    st.subheader("A projekt fázisai")
    phases = content.load_phases()
    for row_start in range(0, len(phases), 3):
        columns = st.columns(3)
        for column, phase in zip(columns, phases[row_start : row_start + 3]):
            with column, st.container(border=True):
                stats = progress.phase_stats(phase)
                st.markdown(f"**{phase['number']}. {phase['title_hu']}**")
                st.caption(phase.get("title_en", ""))
                st.progress(stats["ratio"])
                st.caption(
                    f"{stats['mandatory_done']}/{stats['mandatory_total']} kötelező lépés · "
                    f"{len(phase.get('documents', []))} dokumentum"
                )
                st.markdown(phase.get("tagline", ""))

    st.divider()
    st.subheader("Hogyan használd?")
    st.markdown(meta.get("how_to_use", ""))

    with st.expander("Haladás visszaállítása"):
        st.caption(
            "A pipák a `data/progress.json` fájlban vannak. A törlés nem vonható vissza."
            if progress.persistent()
            else "Demó mód: a pipák csak ebben a böngészőmunkamenetben élnek."
        )
        if st.button("Minden pipa törlése", icon=":material/restart_alt:"):
            progress.reset_all()
            st.success("A haladás törölve.")
            st.rerun()


# ------------------------------------------------------------------------- mintaprojekt

def sample_project() -> None:
    meta = content.load_meta()
    project = meta.get("sample_project", {})

    st.title("Mintaprojekt — " + project.get("name", ""))
    st.caption(project.get("tagline", ""))
    st.markdown(project.get("description", ""))

    if project.get("facts"):
        st.subheader("A projekt alapadatai")
        st.dataframe(
            [{"Megnevezés": key, "Érték": value} for key, value in project["facts"].items()],
            hide_index=True,
            width="stretch",
        )

    if project.get("roles"):
        st.subheader("Szerepkörök és nevek (a mintában végig ezeket használjuk)")
        st.dataframe(
            [
                {
                    "Név": row["name"],
                    "Szerep": row["role"],
                    "Szervezet": row.get("org", ""),
                    "Miért fontos": row.get("note", ""),
                }
                for row in project["roles"]
            ],
            hide_index=True,
            width="stretch",
        )

    idea_doc = content.load_doc_index().get(project.get("idea_doc", ""))
    if idea_doc:
        sample = content.load_sample(idea_doc.get("sample_file"))
        if sample:
            st.divider()
            st.subheader("A projektet elindító dokumentum")
            st.caption(
                f"{idea_doc['name_hu']} ({idea_doc.get('name_en', '')}) — "
                "innen indul a teljes dokumentumlánc."
            )
            tab_preview, tab_source = st.tabs(["Olvasható", "Markdown forrás"])
            with tab_preview:
                st.markdown(sample)
            with tab_source:
                st.code(sample, language="markdown")


# ---------------------------------------------------------------------------- fázisoldal

def make_phase_view(phase_id: str):
    def view() -> None:
        phase = content.phase_by_id(phase_id)
        render.phase_header(phase)
        st.divider()
        render.checklist_block(phase)
        st.divider()
        render.documents_block(phase)
        render.phase_download_block(phase)
        st.divider()
        render.pm_tasks_block(phase)
        render.meetings_block(phase)
        render.data_flow_block(phase)
        render.responsibility_block(phase)
        render.phase_gate(phase)
        render.prince2_block(phase)

        with st.expander("Ennek a fázisnak a pipáit törlöm"):
            if st.button(
                "Fázis haladásának törlése",
                key=f"reset-{phase_id}",
                icon=":material/restart_alt:",
            ):
                progress.reset_phase(phase_id)
                st.rerun()

    return view


# ----------------------------------------------------------------------- dokumentumtérkép

def doc_map() -> None:
    st.title("Dokumentumtérkép")
    st.caption(
        "Melyik dokumentum miből áll össze és mit táplál. "
        "A nyíl a bemenet felől mutat a belőle készülő dokumentum felé. "
        "Egy kör szándékos: a jóváhagyott változáskérelem visszahat a Hatókör-"
        "nyilatkozatra, az Ütemtervre és a Költségvetésre — ez a baseline "
        "új, módosított változata, nem hiba."
    )

    index = content.load_doc_index()
    phases = content.load_phases()

    options = [f"{p['number']}. {p['title_hu']}" for p in phases] + [
        f"Minden fázis ({len(index)} dokumentum)"
    ]
    choice = st.selectbox(
        "Melyik fázist nézzük?",
        options,
        index=0,
        help=(
            "Egy fázist választva a fázis dokumentumai látszanak, "
            "és mellettük azok, amelyekkel közvetlen kapcsolatban állnak. "
            "A gráfot a böngésződ rajzolja ki — egy fázis gyors, a teljes gráf lassabb."
        ),
    )

    if choice.startswith("Minden fázis"):
        st.caption(f"{len(index)} dokumentum, sűrű élhálóval.")
        st.warning(
            f"A teljes gráf kirajzolása a böngésződben történik, és {len(index)} "
            "dokumentumnál ez néhány másodpercig tarthat — lassabb gépen a lap átmenetileg nem reagálhat, "
            "amíg kész. Ha ez zavaró, szűrj inkább egy fázisra fent.",
            icon=":material/hourglass_top:",
        )
        show_full = st.checkbox("Rendben, mutasd a teljes gráfot", value=False)
        if show_full:
            st.graphviz_chart(_build_dot(index, phases, dense=True), width="stretch")
    else:
        focus = phases[options.index(choice)]
        visible = _neighbourhood(index, focus["id"])
        st.caption(
            f"{sum(1 for d in visible.values() if d['phase_id'] == focus['id'])} dokumentum "
            f"ebben a fázisban, {len(visible)} a kapcsolataikkal együtt."
        )
        st.graphviz_chart(_build_dot(visible, phases), width="stretch")

    st.subheader("Teljes dokumentumleltár")
    only_mandatory = st.toggle("Csak a kötelező dokumentumok")
    query = st.text_input("Keresés a dokumentumok között", placeholder="pl. kockázat, charter")

    rows = []
    for doc in sorted(index.values(), key=lambda d: (d["phase_number"], d.get("order", 0))):
        if only_mandatory and not doc.get("mandatory"):
            continue
        haystack = f"{doc.get('name_hu', '')} {doc.get('name_en', '')} {doc.get('why', '')}".lower()
        if query and query.lower() not in haystack:
            continue
        rows.append(
            {
                "Fázis": f"{doc['phase_number']}. {doc['phase_title']}",
                "Dokumentum": doc.get("name_hu", ""),
                "Angol név": doc.get("name_en", ""),
                "Kötelező?": "kötelező" if doc.get("mandatory") else "ajánlott",
                "Bemenete": ", ".join(content.doc_name(r) for r in doc["inputs"]),
                "Mihez bemenet": ", ".join(content.doc_name(r) for r in doc["feeds"]),
                "Van minta?": "igen" if content.load_sample(doc.get("sample_file")) else "készül",
            }
        )

    st.caption(f"{len(rows)} dokumentum")
    st.dataframe(rows, hide_index=True, width="stretch", height=420)


def _neighbourhood(index: dict, phase_id: str) -> dict:
    """Egy fázis dokumentumai + azok, amikkel közvetlen kapcsolatban állnak."""
    core = {i for i, d in index.items() if d["phase_id"] == phase_id}
    visible = set(core)
    for doc_id in core:
        visible.update(index[doc_id]["inputs"])
        visible.update(index[doc_id]["feeds"])
    return {i: index[i] for i in visible if i in index}


def _build_dot(index: dict, phases: list[dict], dense: bool = False) -> str:
    """A DOT-forrás. `dense=True` a nagy (69 csomópontos) gráfhoz: a görbe élek és
    a rétegzett elrendezés helyett egyenes éleket és összevont éleket használ,
    mert a böngésző WASM-mal, a fő szálon rajzolja ki — a görbe illesztés
    ennyi csomópontnál percekig is elhúzódhatna."""
    palette = [
        "#e8f0fe",
        "#e6f4ea",
        "#fef7e0",
        "#fce8e6",
        "#f3e8fd",
        "#e0f7fa",
    ]
    lines = [
        "digraph docmap {",
        "  rankdir=LR;",
        "  splines=" + ("line" if dense else "spline") + ";",
        "  concentrate=" + ("true" if dense else "false") + ";",
        "  nodesep=0.25; ranksep=0.5;",
        "  node [shape=box style=\"rounded,filled\" fontname=\"Helvetica\" fontsize=10];",
        "  edge [color=\"#8b949e\" arrowsize=0.6];",
    ]
    for position, phase in enumerate(phases):
        docs = [d for d in phase.get("documents", []) if d["id"] in index]
        if not docs:
            continue
        fill = palette[position % len(palette)]
        lines.append(f"  subgraph cluster_{phase['id']} {{")
        lines.append(f"    label=\"{phase['number']}. {phase['title_hu']}\";")
        lines.append("    style=\"rounded\"; color=\"#c9d1d9\"; fontsize=11;")
        for doc in docs:
            border = "#d93025" if doc.get("mandatory") else "#9aa0a6"
            label = _wrap(doc.get("name_hu", doc["id"]))
            lines.append(
                f"    \"{doc['id']}\" [label=\"{label}\" fillcolor=\"{fill}\" "
                f"color=\"{border}\"];"
            )
        lines.append("  }")

    seen = set()
    for doc_id, doc in index.items():
        for target in doc["feeds"]:
            if target in index and (doc_id, target) not in seen:
                seen.add((doc_id, target))
                lines.append(f"  \"{doc_id}\" -> \"{target}\";")
    lines.append("}")
    return "\n".join(lines)


def _wrap(text: str, width: int = 22) -> str:
    """Sortörés a gráf csomópontjaiban, hogy a hosszú magyar nevek elférjenek."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        if current and len(current) + 1 + len(word) > width:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return "\\n".join(lines)


# ------------------------------------------------------------------------------ letöltés

def downloads_page() -> None:
    st.title("Letöltések")
    st.caption(
        "Minden minta sima markdown fájl. A zip-ben fázisonkénti almappákban találod őket."
    )

    all_docs = downloads.all_docs_with_samples()
    total_docs = len(content.load_doc_index())

    st.metric("Elkészült minták", f"{len(all_docs)} / {total_docs}")

    if all_docs:
        st.download_button(
            "Teljes csomag letöltése (zip)",
            data=functools.partial(downloads.build_zip, all_docs),  # csak kattintáskor épül
            file_name="pm-mindenes-mintak.zip",
            mime="application/zip",
            icon=":material/folder_zip:",
            type="primary",
        )

    st.divider()
    for phase in content.load_phases():
        phase_docs = downloads.phase_docs_with_samples(phase["id"])
        with st.container(border=True):
            st.markdown(f"**{phase['number']}. {phase['title_hu']}**")
            if not phase_docs:
                st.caption("Ehhez a fázishoz még nem készült kitöltött minta.")
                continue
            st.caption(f"{len(phase_docs)} elkészült minta")
            render.phase_download_block(phase)
            for doc in sorted(phase_docs, key=lambda d: d.get("order", 0)):
                sample = content.load_sample(doc["sample_file"])
                st.download_button(
                    f"{doc['name_hu']} ({doc.get('name_en', '')})",
                    data=sample.encode("utf-8"),
                    file_name=downloads.sample_filename(doc),
                    mime="text/markdown",
                    key=f"dlp-{doc['id']}",
                    icon=":material/description:",
                )


# -------------------------------------------------------------------------------- szótár

def glossary() -> None:
    meta = content.load_meta()
    st.title("Szótár")
    st.caption("Magyar–angol PM fogalomtár, junior nyelven megmagyarázva.")

    query = st.text_input("Keresés", placeholder="pl. WBS, baseline, érintett")

    entries = meta.get("glossary", [])
    if query:
        needle = query.lower()
        entries = [
            e
            for e in entries
            if needle in f"{e['hu']} {e['en']} {e['meaning']}".lower()
        ]

    st.caption(f"{len(entries)} fogalom")
    for entry in entries:
        with st.container(border=True):
            st.markdown(f"**{entry['hu']}** — _{entry['en']}_")
            st.markdown(entry["meaning"])
            if entry.get("example"):
                st.caption(f"A Xyo projektben: {entry['example']}")


# ------------------------------------------------------------------------- PRINCE2

def prince2() -> None:
    data = content.load_prince2()

    st.title(f"{config.BADGE_PRINCE2} PRINCE2 — módszertani kiegészítés")
    st.markdown(data.get("intro", ""))

    tabs = st.tabs(
        [
            "Alapelvek",
            "Folyamatok",
            "Szerepek",
            "Fogalomtár",
            "Mikor melyiket?",
            "A Xyo projekten",
            "Összefoglaló és minták",
        ]
    )
    tab_alap, tab_folyamat, tab_szerep, tab_fogalom, tab_mikor, tab_xyo, tab_doksi = tabs

    # -- Alapelvek ---------------------------------------------------------
    with tab_alap:
        st.subheader("A hét alapelv")
        st.caption(
            "Ha ezek közül bármelyik nem érvényesül, a projekt definíció szerint "
            "nem PRINCE2-projekt — akkor sem, ha minden dokumentum elkészült."
        )
        for number, item in enumerate(data.get("principles", []), start=1):
            with st.container(border=True):
                st.markdown(f"**{number}. {item['name_hu']}** — _{item['name_en']}_")
                st.markdown(item["text"])

        tol = data.get("tolerances", {})
        if tol:
            st.subheader("Toleranciák — a kivételalapú irányítás gyakorlata")
            st.markdown(tol.get("intro", ""))
            st.dataframe(
                [
                    {"Terület": row["area"], "A Xyo projekten így nézne ki": row["xyo"]}
                    for row in tol.get("areas", [])
                ],
                hide_index=True,
                width="stretch",
            )

    # -- Folyamatok --------------------------------------------------------
    with tab_folyamat:
        st.subheader("A hét folyamat — a sorrendiség")
        for item in data.get("processes", []):
            with st.container(border=True):
                st.markdown(
                    f"**{item['code']} — {item['name_hu']}** _({item['name_en']})_"
                )
                st.caption(f"Ki végzi: {item['who']}")
                st.markdown(item["what"])

    # -- Szerepek ----------------------------------------------------------
    with tab_szerep:
        st.subheader("Ki kicsoda a PRINCE2-ben")
        st.dataframe(
            [
                {
                    "Szerep": row["role"],
                    "Magyarul": row.get("role_hu", ""),
                    "Kit képvisel": row.get("represents", ""),
                    "Miért felel": row.get("responsible", ""),
                    "A Xyo projekten": row.get("xyo", ""),
                }
                for row in data.get("roles", [])
            ],
            hide_index=True,
            width="stretch",
            height=340,
        )
        st.info(
            "A **Project Assurance** a PMI-ban nem létezik ilyen formában — és a "
            "valós Xyo projektben sem volt. Ez a legnagyobb hiányzó kontroll: "
            "a Steering Committee kizárólag a projektmenedzser riportjaira "
            "támaszkodott.",
            icon=":material/info:",
        )

    # -- Fogalomtár --------------------------------------------------------
    with tab_fogalom:
        st.subheader("Ugyanaz a dolog, két néven")
        query = st.text_input("Keresés", placeholder="pl. charter, board, tolerancia")
        rows = data.get("concept_map", [])
        if query:
            needle = query.lower()
            rows = [
                r
                for r in rows
                if needle in f"{r['pmi']} {r['prince2']} {r.get('note', '')}".lower()
            ]
        st.dataframe(
            [
                {
                    "PMI / PMBOK": r["pmi"],
                    "PRINCE2": r["prince2"],
                    "Megjegyzés": r.get("note", ""),
                }
                for r in rows
            ],
            hide_index=True,
            width="stretch",
            height=480,
        )

    # -- Mikor melyiket? ---------------------------------------------------
    with tab_mikor:
        left, right = st.columns(2)
        with left:
            st.markdown("### A PRINCE2 akkor erős, ha…")
            for row in data.get("when_prince2", []):
                st.markdown(f"- {row}")
        with right:
            st.markdown("### A PMI akkor erős, ha…")
            for row in data.get("when_pmi", []):
                st.markdown(f"- {row}")
        st.divider()
        st.markdown(data.get("combined", ""))

    # -- A Xyo projekten ---------------------------------------------------
    with tab_xyo:
        stages = data.get("xyo_stages", {})
        st.subheader("Hogyan nézne ki a Xyo projekt PRINCE2 szerint?")
        st.markdown(stages.get("intro", ""))
        st.dataframe(
            [
                {
                    "#": row["num"],
                    "Szakasz": row["name"],
                    "Időszak": row["period"],
                    "A szakaszhatáron": row["gate"],
                }
                for row in stages.get("stages", [])
            ],
            hide_index=True,
            width="stretch",
        )

        already = data.get("already_prince2", {})
        st.subheader("Amit már PRINCE2-szerűen csináltunk")
        st.caption(already.get("intro", ""))
        st.dataframe(
            [
                {"Amit tettünk": r["what"], "PRINCE2-ben ez…": r["p2"]}
                for r in already.get("items", [])
            ],
            hide_index=True,
            width="stretch",
        )

        adds = data.get("would_add", {})
        st.subheader("Amit hozzátett volna")
        st.caption(adds.get("intro", ""))
        gap_icon = {"nagy": "🔴", "közepes": "🟡", "kicsi": "🟢"}
        for row in adds.get("items", []):
            with st.container(border=True):
                st.markdown(f"{gap_icon.get(row['gap'], '')} **{row['what']}**")
                st.caption(f"Mennyire hiányzott: {row['gap']} — {row['note']}")

        st.divider()
        st.markdown(data.get("verdict", ""))

    # -- Összefoglaló és minták -------------------------------------------
    with tab_doksi:
        primer = content.load_sample(data.get("primer_file"))
        if primer:
            st.subheader("Teljes összefoglaló")
            st.caption(
                "Kb. 10 oldal: mi a PRINCE2, miben más a PMI-tól, "
                "mikor melyiket érdemes használni."
            )
            st.download_button(
                "Az összefoglaló letöltése (md)",
                data=primer.encode("utf-8"),
                file_name="prince2-osszefoglalo.md",
                mime="text/markdown",
                icon=":material/download:",
                type="primary",
            )
            if st.toggle("Az összefoglaló megjelenítése", key="show-p2-primer"):
                tab_read, tab_src = st.tabs(["Olvasható", "Markdown forrás"])
                with tab_read:
                    st.markdown(primer)
                with tab_src:
                    st.code(primer, language="markdown")

        st.divider()
        st.subheader("PRINCE2 mintadokumentumok — a Xyo projekt adataival")
        st.caption(
            "Négy dokumentum, amit a PMI-változat nem tartalmaz. Azt mutatják meg, "
            "hogyan nézne ki ugyanez a projekt PRINCE2 szerint."
        )
        for doc in sorted(data.get("documents", []), key=lambda d: d.get("order", 0)):
            sample = content.load_sample(doc.get("sample_file"))
            with st.expander(f"**{doc['name_hu']}** ({doc.get('name_en', '')})"):
                st.markdown(f"**Mire jó?**  \n{doc['why']}")
                st.markdown(f"**PMI-megfelelő:** {doc.get('pmi', '—')}")
                if sample is None:
                    st.info(
                        "A minta még nem készült el.",
                        icon=":material/hourglass_empty:",
                    )
                    continue
                st.divider()
                left, right = st.columns([2, 1])
                with left:
                    show = st.toggle(
                        "A minta megjelenítése",
                        key=f"show-{doc['id']}",
                        help=(
                            "A minta csak igény szerint töltődik be, "
                            "hogy az oldal gyors maradjon."
                        ),
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
                    tab_read, tab_src = st.tabs(["Olvasható", "Markdown forrás"])
                    with tab_read:
                        st.markdown(sample)
                    with tab_src:
                        st.code(sample, language="markdown")
