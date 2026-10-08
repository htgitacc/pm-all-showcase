"""Füstteszt: minden oldal kivétel nélkül lefut, a letöltési csomag teljes."""

from __future__ import annotations

import io
import zipfile

import pytest
from streamlit.testing.v1 import AppTest

from pm_app import content, downloads

PAGES = ["overview", "sample_project", "doc_map", "downloads_page", "glossary", "prince2"]
PHASES = ["initiation", "planning", "execution", "monitoring", "closure", "benefits"]


def _run(script: str) -> AppTest:
    return AppTest.from_string(script, default_timeout=60).run()


@pytest.mark.parametrize("page", PAGES)
def test_page_renders(page, tmp_progress):
    at = _run(f"from pm_app import views\nviews.{page}()\n")
    assert not at.exception, at.exception


@pytest.mark.parametrize("phase_id", PHASES)
def test_phase_page_renders(phase_id, tmp_progress):
    at = _run(f"from pm_app import views\nviews.make_phase_view({phase_id!r})()\n")
    assert not at.exception, at.exception


def test_full_app_renders(tmp_progress):
    at = AppTest.from_file("../app.py", default_timeout=60).run()
    assert not at.exception, at.exception


def test_full_zip_contains_every_sample():
    docs = downloads.all_docs_with_samples()
    archive = zipfile.ZipFile(io.BytesIO(downloads.build_zip(docs)))
    names = archive.namelist()
    assert len(docs) == len(content.load_doc_index())
    assert len(names) == len(set(names)) == len(docs) + 1  # + OLVASSEL.txt
    assert "OLVASSEL.txt" in names
