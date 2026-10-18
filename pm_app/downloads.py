"""Minta md fájlok letöltése egyesével és zip csomagban."""

from __future__ import annotations

import io
import zipfile
from datetime import date
from pathlib import Path

from pm_app import config, content


def sample_filename(doc: dict) -> str:
    sample = doc.get("sample_file")
    if sample:
        return (config.ROOT / sample).name
    return f"{doc['id']}.md"


def build_zip(docs: list[dict]) -> bytes:
    """Zip a megadott dokumentumok mintáiból, fázis szerinti almappákban."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for doc in docs:
            text = content.load_sample(doc.get("sample_file"))
            if text is None:
                continue
            arcname = f"{doc['phase_number']}-{doc['phase_id']}/{sample_filename(doc)}"
            archive.writestr(arcname, text)
        archive.writestr("OLVASSEL.txt", _readme_text(docs))
    return buffer.getvalue()


def _readme_text(docs: list[dict]) -> str:
    lines = [
        "PM-mindenes — letöltött dokumentumminták",
        f"Készült: {date.today().isoformat()}",
        f"Mintaprojekt: {content.sample_projects()[0]['name']}",
        "",
        "Tartalom:",
    ]
    for doc in docs:
        if content.load_sample(doc.get("sample_file")) is None:
            continue
        lines.append(
            f"  {doc['phase_number']}-{doc['phase_id']}/{sample_filename(doc)}"
            f"  —  {doc.get('name_hu')} ({doc.get('name_en')})"
        )
    return "\n".join(lines) + "\n"


def example_docs(project_id: str) -> list[dict]:
    """Egy további (nem elsődleges) mintaprojekt dokumentumai, sorrendben, a mintájuk útvonalával."""
    found = []
    for doc in content.load_doc_index().values():
        example = next((e for e in content.doc_examples(doc) if e["id"] == project_id), None)
        if example:
            found.append({**doc, "example_path": example["path"]})
    return sorted(found, key=lambda d: (d["phase_number"], d.get("order", 0), d["id"]))


def build_example_zip(project_id: str) -> bytes:
    """Egy további mintaprojekt csomagja: fázis szerinti almappák, a projekt azonosítójával
    előtagolt fájlnevek (ugyanúgy, mint a kártyán letöltve), és OLVASSEL a projekt nevével."""
    project = next(p for p in content.sample_projects() if p["id"] == project_id)
    docs = example_docs(project_id)
    names = {d["id"]: f"{d['phase_number']}-{d['phase_id']}/{project_id}-{Path(d['example_path']).name}" for d in docs}
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for doc in docs:
            archive.writestr(names[doc["id"]], content.load_sample(doc["example_path"]))
        lines = [
            "PM-mindenes — letöltött dokumentumminták",
            f"Készült: {date.today().isoformat()}",
            f"Mintaprojekt: {project['name']}",
            "",
            "Tartalom:",
            *(f"  {names[d['id']]}  —  {d.get('name_hu')} ({d.get('name_en')})" for d in docs),
        ]
        archive.writestr("OLVASSEL.txt", "\n".join(lines) + "\n")
    return buffer.getvalue()


def phase_docs_with_samples(phase_id: str) -> list[dict]:
    return [
        d
        for d in content.load_doc_index().values()
        if d["phase_id"] == phase_id and content.load_sample(d.get("sample_file")) is not None
    ]


def all_docs_with_samples() -> list[dict]:
    docs = [
        d
        for d in content.load_doc_index().values()
        if content.load_sample(d.get("sample_file")) is not None
    ]
    return sorted(docs, key=lambda d: (d["phase_number"], d.get("order", 0), d["id"]))
