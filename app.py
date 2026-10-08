"""PM-mindenes — Streamlit belépőpont.

Indítás:  streamlit run app.py
"""

import streamlit as st

from pm_app import config, content, gantt, progress, views

st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=":material/checklist:",
    layout="wide",
    initial_sidebar_state="expanded",
)

progress.state()  # a pipák betöltése fájlból az első futásnál

PHASE_ICONS = {
    1: ":material/rocket_launch:",
    2: ":material/architecture:",
    3: ":material/construction:",
    4: ":material/monitoring:",
    5: ":material/task_alt:",
    6: ":material/insights:",
}


def _phase_pages() -> list:
    pages = []
    for phase in content.load_phases():
        pages.append(
            st.Page(
                views.make_phase_view(phase["id"]),
                title=f"{phase['number']}. {phase['title_hu']}",
                url_path=f"fazis-{phase['number']}-{phase['id']}",
                icon=PHASE_ICONS.get(phase["number"], ":material/circle:"),
            )
        )
    return pages


navigation = st.navigation(
    {
        "Kezdés": [
            st.Page(
                views.overview,
                title="Áttekintés",
                icon=":material/home:",  # alapértelmezett oldal: a gyökér-URL-en él
                default=True,
            ),
            st.Page(
                views.sample_project,
                title="Mintaprojekt — Xyo Kft.",
                url_path="mintaprojekt",
                icon=":material/business:",
            ),
        ],
        "Fázisok": _phase_pages(),
        "Segédletek": [
            st.Page(
                views.doc_map,
                title="Dokumentumtérkép",
                url_path="dokumentumterkep",
                icon=":material/account_tree:",
            ),
            st.Page(
                gantt.view,
                title="Gantt-nézet",
                url_path="gantt",
                icon=":material/view_timeline:",
            ),
            st.Page(
                views.downloads_page,
                title="Letöltések",
                url_path="letoltesek",
                icon=":material/download:",
            ),
            st.Page(
                views.glossary,
                title="Szótár",
                url_path="szotar",
                icon=":material/menu_book:",
            ),
        ],
        "Módszertan": [
            st.Page(
                views.prince2,
                title="PRINCE2",
                url_path="prince2",
                icon=":material/compare_arrows:",
            ),
        ],
    },
    expanded=True,  # 12 oldal felett a Streamlit „View X more" mögé rejtené a menü végét
)

with st.sidebar:
    st.markdown(f"### {config.APP_TITLE}")
    st.progress(progress.overall_ratio(), text=f"Haladás: {progress.overall_ratio():.0%}")
    st.caption("Mintaprojekt: Xyo Kft. — cloud-first pilot")
    if not progress.persistent():
        st.caption(":material/info: Demó mód: a pipák csak ebben a munkamenetben élnek.")

    problems = content.validate()
    if problems:
        with st.expander(f":material/error: Tartalmi hibák ({len(problems)})"):
            for problem in problems:
                st.markdown(f"- {problem}")

navigation.run()
