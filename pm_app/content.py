"""Tartalombetöltés: a fázisok YAML-jai, a metaadatok és a dokumentum-index."""

from __future__ import annotations

import yaml
import streamlit as st

from pm_app import config


def _read_yaml(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


@st.cache_data(show_spinner=False)
def load_meta() -> dict:
    """A meta.yaml: fázissorrend, szerepkörök, glosszárium, mintaprojekt."""
    return _read_yaml(config.META_FILE)


@st.cache_data(show_spinner=False)
def load_prince2() -> dict:
    """A PRINCE2 kiegészítő réteg tartalma (content/prince2.yaml)."""
    return _read_yaml(config.PRINCE2_FILE)


@st.cache_data(show_spinner=False)
def load_phases() -> list[dict]:
    """Minden fázis YAML-ja, `number` szerint rendezve."""
    phases = []
    for path in sorted(config.PHASES_DIR.glob("*.yaml")):
        phase = _read_yaml(path)
        phase["_source"] = path.name
        phases.append(phase)
    return sorted(phases, key=lambda p: p.get("number", 99))


@st.cache_data(show_spinner=False)
def load_doc_index() -> dict:
    """id -> dokumentum, kiegészítve a fázis adataival és a visszafelé mutató élekkel."""
    index: dict[str, dict] = {}
    for phase in load_phases():
        for doc in phase.get("documents", []):
            entry = dict(doc)
            entry["phase_id"] = phase["id"]
            entry["phase_number"] = phase.get("number")
            entry["phase_title"] = phase.get("title_hu")
            entry.setdefault("inputs", [])
            entry.setdefault("feeds", [])
            index[doc["id"]] = entry

    # Az `inputs` és `feeds` élek szimmetrikus kiegészítése, hogy a térkép teljes legyen.
    for doc_id, doc in index.items():
        for target in doc["feeds"]:
            if target in index and doc_id not in index[target]["inputs"]:
                index[target]["inputs"].append(doc_id)
        for source in doc["inputs"]:
            if source in index and doc_id not in index[source]["feeds"]:
                index[source]["feeds"].append(doc_id)
    return index


@st.cache_data(show_spinner=False)
def load_sample(rel_path: str) -> str | None:
    """Egy minta md fájl tartalma, vagy None, ha még nem készült el."""
    if not rel_path:
        return None
    path = config.ROOT / rel_path
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def validate() -> list[str]:
    """Indításkori ellenőrzés: törött hivatkozások és hiányzó mintafájlok."""
    problems: list[str] = []
    index = load_doc_index()

    for doc_id, doc in index.items():
        for ref in doc["inputs"] + doc["feeds"]:
            if ref not in index:
                problems.append(f"`{doc_id}`: ismeretlen dokumentum-hivatkozás → `{ref}`")
        sample = doc.get("sample_file")
        if sample and not (config.ROOT / sample).exists():
            problems.append(f"`{doc_id}`: hiányzó mintafájl → `{sample}`")

    for phase in load_phases():
        for item in phase.get("checklist", []):
            refs = doc_refs(item)
            for ref in refs:
                if ref not in index:
                    problems.append(
                        f"`{phase['id']}` / `{item['id']}`: ismeretlen doc_ref → `{ref}`"
                    )
            # Kötelező lépés kimenete nem lehet kizárólag ajánlott dokumentum.
            known = [index[r] for r in refs if r in index]
            if item.get("mandatory", True) and known and not any(d.get("mandatory") for d in known):
                problems.append(
                    f"`{phase['id']}` / `{item['id']}`: kötelező lépés, de minden "
                    "kimenete ajánlott dokumentum"
                )

    # A PRINCE2-réteg mintafájljai
    prince2 = load_prince2()
    for path_key in ("primer_file",):
        rel = prince2.get(path_key)
        if rel and not (config.ROOT / rel).exists():
            problems.append(f"PRINCE2 `{path_key}`: hiányzó fájl → `{rel}`")
    for doc in prince2.get("documents", []):
        sample = doc.get("sample_file")
        if sample and not (config.ROOT / sample).exists():
            problems.append(f"PRINCE2 `{doc['id']}`: hiányzó mintafájl → `{sample}`")
    return problems


def doc_refs(item: dict) -> list[str]:
    """Egy checklist-elem kimeneti dokumentumai — a `doc_ref` lehet egy id vagy lista."""
    ref = item.get("doc_ref")
    if not ref:
        return []
    return [ref] if isinstance(ref, str) else list(ref)


def phase_by_id(phase_id: str) -> dict | None:
    for phase in load_phases():
        if phase["id"] == phase_id:
            return phase
    return None


def doc_name(doc_id: str) -> str:
    """Olvasható név egy dokumentum-id-hez, a térképhez és a kereszthivatkozásokhoz."""
    doc = load_doc_index().get(doc_id)
    if not doc:
        return doc_id
    return doc.get("name_hu", doc_id)


def docs_with_samples() -> list[dict]:
    return [d for d in load_doc_index().values() if d.get("sample_file")]
