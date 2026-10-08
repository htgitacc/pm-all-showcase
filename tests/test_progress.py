"""A checklist-haladás tárolása és a törlés viselkedése."""

from __future__ import annotations

import json

from streamlit.testing.v1 import AppTest

from pm_app import config, progress

PHASE_SCRIPT = """
from pm_app import views
views.make_phase_view("initiation")()
"""


def _phase_app() -> AppTest:
    at = AppTest.from_string(PHASE_SCRIPT, default_timeout=60)
    return at.run()


def _reset_button(at: AppTest):
    return next(b for b in at.button if b.label.startswith("Fázis haladásának"))


def test_check_is_saved_to_file(tmp_progress):
    at = _phase_app()
    at.checkbox(key="cb-init-01").check().run()
    assert json.loads(tmp_progress.read_text(encoding="utf-8")) == {"init-01": True}


def test_phase_reset_clears_state_file_and_widget(tmp_progress):
    at = _phase_app()
    at.checkbox(key="cb-init-01").check().run()
    _reset_button(at).click().run()

    assert at.checkbox(key="cb-init-01").value is False  # a korábbi hiba: True maradt
    assert "init-01" not in at.session_state["progress"]
    assert json.loads(tmp_progress.read_text(encoding="utf-8")) == {}


def test_phase_reset_keeps_other_phases(tmp_progress):
    tmp_progress.write_text(json.dumps({"plan-01": True}), encoding="utf-8")
    at = _phase_app()
    at.checkbox(key="cb-init-01").check().run()
    _reset_button(at).click().run()
    assert json.loads(tmp_progress.read_text(encoding="utf-8")) == {"plan-01": True}


def test_two_sessions_do_not_overwrite_each_other(tmp_progress):
    first, second = _phase_app(), _phase_app()  # mindkettő üres állapotot olvasott be
    first.checkbox(key="cb-init-01").check().run()
    second.checkbox(key="cb-init-02").check().run()
    saved = json.loads(tmp_progress.read_text(encoding="utf-8"))
    assert saved == {"init-01": True, "init-02": True}


def test_session_mode_never_touches_the_file(tmp_progress, monkeypatch):
    monkeypatch.setattr(config, "STORAGE_MODE", "session")
    tmp_progress.write_text(json.dumps({"init-01": True}), encoding="utf-8")

    at = _phase_app()
    assert at.checkbox(key="cb-init-01").value is False  # nem a közös fájlból indul
    at.checkbox(key="cb-init-02").check().run()
    assert json.loads(tmp_progress.read_text(encoding="utf-8")) == {"init-01": True}


def test_phase_stats_counts_only_mandatory_in_ratio():
    phase = {
        "checklist": [
            {"id": "a", "mandatory": True},
            {"id": "b", "mandatory": True},
            {"id": "c", "mandatory": False},
        ]
    }
    done = {"a": True, "c": True}
    original = progress.is_done
    try:
        progress.is_done = lambda item_id: done.get(item_id, False)
        stats = progress.phase_stats(phase)
    finally:
        progress.is_done = original
    assert stats["ratio"] == 0.5
    assert (stats["mandatory_done"], stats["optional_done"]) == (1, 1)
