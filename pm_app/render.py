"""Újrafelhasználható UI blokkok a fázisoldalakhoz."""

from __future__ import annotations

import functools

import streamlit as st

from pm_app import config, content, downloads, progress


def text_table(rows: list[dict], height: int | None = None) -> None:
    """Hosszabb szöveget tartalmazó tábla.

    Az `st.dataframe` rács-alapú, a cellaszöveget nem tördeli, hanem levágja;
    az `st.table` HTML-táblát rajzol, amely a szűk oszlopban több sorba tör.
    A `height` görgethető, rögzített magasságú keretet ad (pl. a hosszú fogalomtárhoz).
    """
    st.table(rows, hide_index=True, height=height if height else "content")


# --------------------------------------------------------------------------- fejléc

def phase_header(phase: dict) -> None:
    stats = progress.phase_stats(phase)
    st.title(f"{phase['number']}. {phase['title_hu']}")
    st.caption(f"{phase.get('title_en', '')} · {phase.get('tagline', '')}")

    st.progress(
        stats["ratio"],
        text=(
            f"Kötelező lépések: {stats['mandatory_done']}/{stats['mandatory_total']}"
            f"  ·  ajánlott: {stats['optional_done']}/{stats['optional_total']}"
        ),
    )

    if phase.get("purpose"):
        st.markdown(phase["purpose"])

    if phase.get("when"):
        st.info(f"**Mikor tartunk itt?** {phase['when']}", icon=":material/schedule:")


def phase_gate(phase: dict) -> None:
    gate = phase.get("gate")
    if not gate:
        return
    st.subheader("Fázis-kapu (Phase Gate) — mit kell felmutatni a továbblépéshez")
    st.warning(gate.get("summary", ""), icon=":material/flag:")
    for crit in gate.get("criteria", []):
        st.markdown(f"- {crit}")
    if gate.get("decision_by"):
        st.caption(f"A döntést hozza: {gate['decision_by']}")


# ---------------------------------------------------------------------- 1. PM feladatai

def pm_tasks_block(phase: dict) -> None:
    tasks = phase.get("pm_tasks")
    if not tasks:
        return
    st.subheader("A projektmenedzser feladatai ebben a fázisban")
    for task in tasks:
        with st.container(border=True):
            st.markdown(f"**{task['text']}**")
            if task.get("why"):
                st.caption(f"Miért: {task['why']}")


# ------------------------------------------------------------------------ 2. meetingek

def meetings_block(phase: dict) -> None:
    meetings = phase.get("meetings")
    if not meetings:
        return
    st.subheader("Meetingek — mit kell megszervezni és kiket kell meghívni")
    for meeting in meetings:
        title = meeting["name_hu"]
        if meeting.get("name_en"):
            title += f" ({meeting['name_en']})"
        with st.expander(title):
            st.markdown(f"**Cél:** {meeting['purpose']}")
            if meeting.get("when"):
                st.markdown(f"**Mikor / milyen gyakran:** {meeting['when']}")
            if meeting.get("duration"):
                st.markdown(f"**Időtartam:** {meeting['duration']}")
            if meeting.get("participants"):
                st.markdown("**Kiket hívj meg:**")
                for person in meeting["participants"]:
                    st.markdown(f"- {person}")
            if meeting.get("agenda"):
                st.markdown("**Napirend:**")
                for point in meeting["agenda"]:
                    st.markdown(f"- {point}")
            if meeting.get("output"):
                st.markdown(f"**Kimenete:** {meeting['output']}")
            if meeting.get("tip"):
                st.info(meeting["tip"], icon=":material/lightbulb:")


# ------------------------------------------------------- 3. adat be / ki / nem kiadható

def data_flow_block(phase: dict) -> None:
    data_in = phase.get("data_in")
    data_out = phase.get("data_out")
    restricted = phase.get("data_restricted")
    if not (data_in or data_out or restricted):
        return

    st.subheader("Adatáramlás — kitől kérsz be, kinek adsz ki, mit nem adhatsz ki")

    if data_in:
        st.markdown("**Amit be kell kérned:**")
        text_table(
            [
                {
                    "Kitől": row["from"],
                    "Mit": row["what"],
                    "Mihez kell": _doc_names(row.get("used_in")),
                    "Mire figyelj": row.get("note", ""),
                }
                for row in data_in
            ],
        )

    if data_out:
        st.markdown("**Amit szolgáltatnod kell:**")
        text_table(
            [
                {
                    "Kinek": row["to"],
                    "Mit": row["what"],
                    "Mikor": row.get("when", ""),
                    "Formátum / forrás": row.get("note", ""),
                }
                for row in data_out
            ],
        )

    if restricted:
        st.markdown("**Amit NEM adhatsz ki:**")
        for row in restricted:
            st.error(f"**{row['what']}** — {row['why']}", icon=":material/lock:")


def _doc_names(refs) -> str:
    if not refs:
        return ""
    if isinstance(refs, str):
        refs = [refs]
    return ", ".join(content.doc_name(ref) for ref in refs)


# ----------------------------------------------------------------------- 4. felelősség

def responsibility_block(phase: dict) -> None:
    resp = phase.get("responsibility")
    if not resp:
        return
    st.subheader("Felelősség — miért és meddig te felelsz")
    if resp.get("summary"):
        st.markdown(resp["summary"])
    for item in resp.get("items", []):
        with st.container(border=True):
            st.markdown(f"**{item['what']}**")
            if item.get("risk"):
                st.caption(f"Ha elmarad: {item['risk']}")


# -------------------------------------------------------------------- 6. dokumentumok

def documents_block(phase: dict) -> None:
    docs = phase.get("documents")
    if not docs:
        return

    index = content.load_doc_index()
    st.subheader("Elkészítendő dokumentumok")
    st.caption(
        "A :red-badge[kötelező] jelölésűek nélkül a fázis nem tekinthető lezártnak. "
        f"Az :gray-badge[ajánlott] jelölésűekre igaz: {config.OPTIONAL_HINT}"
    )

    for doc in docs:
        entry = index[doc["id"]]
        badge = config.BADGE_MANDATORY if doc.get("mandatory") else config.BADGE_OPTIONAL
        sample = content.load_sample(doc.get("sample_file"))
        marker = "" if sample else "  ·  _minta még készül_"
        label = f"{badge} **{doc['name_hu']}** ({doc.get('name_en', '')}){marker}"

        with st.expander(label):
            _document_body(entry, sample)


def _document_body(doc: dict, sample: str | None) -> None:
    if doc.get("why"):
        st.markdown(f"**Mire jó, és mitől véd meg?**  \n{doc['why']}")

    if doc.get("owner"):
        st.markdown(f"**Ki készíti / ki hagyja jóvá:** {doc['owner']}")

    if doc.get("contents"):
        st.markdown("**Mit tartalmaz?**")
        for row in doc["contents"]:
            st.markdown(f"- {row}")

    left, right = st.columns(2)
    with left:
        st.markdown("**Bemenete (miből áll össze):**")
        if doc["inputs"]:
            for ref in doc["inputs"]:
                st.markdown(f"- {content.doc_name(ref)}")
        else:
            st.caption("Nincs projekten belüli előzménye — ez kiindulási dokumentum.")
    with right:
        st.markdown("**Mihez lesz bemenet:**")
        if doc["feeds"]:
            for ref in doc["feeds"]:
                st.markdown(f"- {content.doc_name(ref)}")
        else:
            st.caption("Végpont: nem táplál további dokumentumot.")

    if doc.get("pitfall"):
        st.warning(f"**Tipikus hiba:** {doc['pitfall']}", icon=":material/warning:")

    if sample is None:
        st.info(
            "Ehhez a dokumentumhoz a kitöltött Xyo-minta még nem készült el.",
            icon=":material/hourglass_empty:",
        )
        return

    st.divider()

    left, right = st.columns([2, 1])
    with left:
        show = st.toggle(
            "Kitöltött minta megjelenítése — Xyo Kft.",
            key=f"show-{doc['id']}",
            help="A minta csak igény szerint töltődik be, hogy az oldal gyors maradjon.",
        )
    with right:
        st.download_button(
            "Letöltés md fájlként",
            data=sample.encode("utf-8"),
            file_name=downloads.sample_filename(doc),
            mime="text/markdown",
            key=f"dl-{doc['id']}",
            icon=":material/download:",
        )

    if not show:
        return

    tab_preview, tab_source = st.tabs(["Olvasható", "Markdown forrás (másolható)"])
    with tab_preview:
        st.markdown(sample)
    with tab_source:
        st.code(sample, language="markdown")


# -------------------------------------------------------------------------- checklist

def checklist_block(phase: dict) -> None:
    items = phase.get("checklist")
    if not items:
        return

    index = content.load_doc_index()
    st.subheader("Checklist — a fázis lépései sorrendben")

    for number, item in enumerate(items, start=1):
        item_id = item["id"]
        widget_key = progress.widget_key(item_id)
        badge = config.BADGE_MANDATORY if item.get("mandatory", True) else config.BADGE_OPTIONAL

        with st.container(border=True):
            st.checkbox(
                f"{badge}  **{number}. {item['text']}**",
                value=progress.is_done(item_id),
                key=widget_key,
                on_change=progress.toggle,
                args=(item_id, widget_key),
            )

            refs = content.doc_refs(item)
            if refs:
                names = []
                for ref in refs:
                    doc = index.get(ref, {})
                    name = doc.get("name_hu", ref)
                    if len(refs) > 1 and doc and not doc.get("mandatory"):
                        name += " (ajánlott)"
                    names.append(name)
                st.caption(f"Kimenete: {' · '.join(names)}")

            if item.get("why") or item.get("how"):
                with st.expander("Miért és hogyan?"):
                    if item.get("why"):
                        st.markdown(f"**Miért:** {item['why']}")
                    if item.get("how"):
                        st.markdown("**Hogyan:**")
                        for step in item["how"]:
                            st.markdown(f"- {step}")
                    if item.get("tip"):
                        st.info(item["tip"], icon=":material/lightbulb:")


# ----------------------------------------------------------------- fázis-szintű letöltés

def phase_download_block(phase: dict) -> None:
    docs = downloads.phase_docs_with_samples(phase["id"])
    if not docs:
        return
    st.download_button(
        f"A fázis összes mintája zip-ben ({len(docs)} dokumentum)",
        data=functools.partial(downloads.build_zip, docs),  # csak kattintáskor épül
        file_name=f"pm-mindenes-{phase['number']}-{phase['id']}.zip",
        mime="application/zip",
        key=f"zip-{phase['id']}",
        icon=":material/folder_zip:",
    )


# ------------------------------------------------------- PRINCE2-kiegészítés

def prince2_block(phase: dict) -> None:
    """A fázis PRINCE2-megfelelője — jelölt, elkülönített kiegészítő réteg."""
    block = phase.get("prince2")
    if not block:
        return

    st.divider()
    st.subheader(f"{config.BADGE_PRINCE2} Módszertani kiegészítés")
    st.caption(config.PRINCE2_NOTE)

    with st.expander("Mi ez a fázis PRINCE2-ben?"):
        codes = " · ".join(
            f"**{p['code']}** — {p['name']}" for p in block.get("processes", [])
        )
        st.markdown(f"**Megfelelő PRINCE2-folyamat:**  \n{codes}")

        if block.get("summary"):
            st.markdown(block["summary"])

        if block.get("adds"):
            st.markdown("**Mit tenne hozzá?**")
            for item in block["adds"]:
                with st.container(border=True):
                    st.markdown(f"**{item['what']}**")
                    st.caption(item["why"])

        if block.get("products"):
            st.markdown("**PRINCE2 irányítási termékek ebben a fázisban:**")
            text_table(
                [
                    {
                        "PRINCE2 termék": row["name_hu"],
                        "Angolul": row.get("name_en", ""),
                        "PMI-megfelelő": row.get("pmi", ""),
                    }
                    for row in block["products"]
                ],
            )

        st.caption(
            "A teljes összefoglaló és a négy PRINCE2-mintadokumentum "
            "a **PRINCE2** oldalon található."
        )
