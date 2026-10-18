"""A checklist-haladás tárolása és a törlés viselkedése."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from pm_app import config, content, progress

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


def test_reset_all_confirms_after_the_rerun(tmp_progress):
    at = AppTest.from_string("from pm_app import views\nviews.overview()\n", default_timeout=60).run()
    next(b for b in at.button if b.label == "Minden pipa törlése").click().run()
    assert not at.exception, at.exception
    assert [s.value for s in at.success] == ["A haladás törölve."]  # a korábbi hiba: a rerun elnyelte
    assert at.run().success.len == 0  # csak egyszer jelenik meg


@pytest.mark.parametrize(
    "env, root, expected",
    [
        ({"PM_MINDENES_STORAGE": "session"}, "/home/tibor/pm-all", "session"),
        ({"PM_MINDENES_STORAGE": " File "}, "/mount/src/pm-all-showcase", "file"),  # a beállítás dönt
        ({}, "/home/tibor/pm-all", "file"),                                         # helyben tartós
        ({}, "/mount/src/pm-all-showcase", "session"),                              # Cloud: kimaradt Secrets-sor
        ({"PM_MINDENES_STORAGE": "sesion"}, "/mount/src/pm-all-showcase", "session"),  # elgépelés a Cloudon
        ({"PM_MINDENES_STORAGE": "sesion"}, "/home/tibor/pm-all", "file"),
    ],
)
def test_storage_mode_is_safe_when_the_setting_is_missing(env, root, expected):
    assert config.storage_mode(env, Path(root)) == expected


def test_interrupted_write_keeps_the_previous_file(tmp_progress, monkeypatch):
    # Írás közbeni leállás: a régi haladásfájl ép marad, nem lesz félig írt JSON.
    tmp_progress.write_text(json.dumps({"init-01": True}), encoding="utf-8")
    original_write = Path.write_text

    def crash_midway(self, text, *args, **kwargs):
        original_write(self, text[: len(text) // 2], *args, **kwargs)
        raise OSError("a lemez megtelt")

    monkeypatch.setattr(Path, "write_text", crash_midway)
    with pytest.raises(OSError):
        progress._write_to_disk({"init-01": True, "init-02": True})
    monkeypatch.undo()

    assert json.loads(tmp_progress.read_text(encoding="utf-8")) == {"init-01": True}
    assert [p.name for p in tmp_progress.parent.iterdir()] == ["progress.json"]  # nem marad ideiglenes fájl


# ----------------------------------------------------------- mentés és visszatöltés

KNOWN = {"init-01", "init-02", "plan-01"}


def _export(done, day=dt.date(2026, 10, 18)) -> bytes:
    return progress.build_export(done, day)


def test_export_roundtrip_keeps_exactly_the_checked_items():
    preview = progress.parse_import(_export(["plan-01", "init-01"]), KNOWN)
    assert preview == progress.ImportPreview(done=("init-01", "plan-01"), unknown=0, exported="2026-10-18")


def test_unknown_ids_are_skipped_and_only_counted():
    # pl. egy régebbi tartalomverzió mentése; a fájl szövege nem kerülhet ki a felületre
    preview = progress.parse_import(_export(["init-01", "<b>régi-99</b>", "x-1"]), KNOWN)
    assert preview.done == ("init-01",)
    assert preview.unknown == 2


@pytest.mark.parametrize(
    "raw",
    [
        b"nem json",
        b"\xff\xfe\x00",                                                   # nem UTF-8
        b"[]",                                                             # nem objektum
        json.dumps({"format": "mas-alkalmazas", "version": 1, "done": []}).encode(),
        json.dumps({"format": "pm-mindenes-haladas", "version": 2, "done": []}).encode(),
        json.dumps({"format": "pm-mindenes-haladas", "version": 1, "done": "init-01"}).encode(),
        json.dumps({"format": "pm-mindenes-haladas", "version": 1, "done": [1, 2]}).encode(),
        json.dumps({"format": "pm-mindenes-haladas", "version": 1}).encode(),  # nincs done
    ],
)
def test_invalid_files_are_rejected(raw):
    with pytest.raises(progress.InvalidProgressFile):
        progress.parse_import(raw, KNOWN)


def test_oversized_file_is_rejected_before_parsing():
    raw = _export(["init-01"]) + b" " * progress.MAX_IMPORT_BYTES
    with pytest.raises(progress.InvalidProgressFile, match="túl nagy"):
        progress.parse_import(raw, KNOWN)


@pytest.mark.parametrize("exported", ["tegnap", 20261018, None])
def test_unreadable_export_date_is_ignored(exported):
    raw = json.dumps({"format": "pm-mindenes-haladas", "version": 1, "exported": exported, "done": []}).encode()
    assert progress.parse_import(raw, KNOWN).exported == ""


def test_known_ids_are_the_checklist_items():
    assert {"init-01", "plan-01"} <= progress.known_item_ids()
    assert len(progress.known_item_ids()) == sum(len(p["checklist"]) for p in content.load_phases())


IMPORT_SCRIPT = """
import streamlit as st
from pm_app import progress, views
if st.session_state.get("do_import"):
    progress.apply_import(progress.ImportPreview(done=("init-02",), unknown=0, exported=""))
    st.session_state.do_import = False
views.make_phase_view("initiation")()
"""


def test_import_replaces_current_progress_and_saves_it(tmp_progress):
    at = AppTest.from_string(IMPORT_SCRIPT, default_timeout=60).run()
    at.checkbox(key="cb-init-01").check().run()
    at.session_state["do_import"] = True
    at.run()
    assert at.checkbox(key="cb-init-01").value is False  # felülírás, nem összefésülés
    assert at.checkbox(key="cb-init-02").value is True
    assert json.loads(tmp_progress.read_text(encoding="utf-8")) == {"init-02": True}


def test_overview_offers_backup_and_restore(tmp_progress):
    at = AppTest.from_string("from pm_app import views\nviews.overview()\n", default_timeout=60).run()
    assert not at.exception, at.exception
    labels = [e.proto.label for e in at.get("download_button")]
    assert "Haladás mentése (JSON)" in labels
    uploaders = at.get("file_uploader")
    assert len(uploaders) == 1 and list(uploaders[0].proto.type) == [".json"]


def test_upload_limit_is_small():
    # Az egyetlen feltöltés a néhány KB-os mentés; a nyilvános demón ne fogadjunk 200 MB-ot.
    import tomllib

    cfg = tomllib.loads((config.ROOT / ".streamlit" / "config.toml").read_text(encoding="utf-8"))
    assert cfg["server"]["maxUploadSize"] <= 1


@pytest.mark.parametrize(
    "mode, expected, absent",
    [
        ("file", "data/progress.json", "mentsd el"),
        ("session", "mentsd el", "data/progress.json"),  # a demón nincs progress.json
    ],
)
def test_how_to_use_matches_the_storage_mode(mode, expected, absent, tmp_progress, monkeypatch):
    monkeypatch.setattr(config, "STORAGE_MODE", mode)
    at = AppTest.from_string("from pm_app import views\nviews.overview()\n", default_timeout=60).run()
    how_to = next(m.value for m in at.markdown if "Pipáld ki, ami kész" in m.value)
    assert expected in how_to
    assert absent not in how_to
    assert "{storage_note}" not in how_to
