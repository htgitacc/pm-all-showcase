"""Minta md fájlok letöltése egyesével és zip csomagban."""

from __future__ import annotations

import io
import zipfile
from datetime import date

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
        "Mintaprojekt: Xyo Kft. — cloud-first pilot",
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
