"""Continuity helpers for Ω∞v."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]

ARTIFACT_PATHS = {
    "root_continuity_pack": ROOT / "CONTINUITY_PACK.md",
    "continuity_pack": ROOT / "continuity" / "continuity_pack.md",
    "charter": ROOT / "CHARTER.md",
    "doctrine": ROOT / "DOCTRINE.md",
    "brand_charter": ROOT / "brand" / "charter.md",
}


def find_continuity_documents() -> Dict[str, str]:
    """Return the content of the repository's continuity-related documents."""
    docs: Dict[str, str] = {}
    for key, path in ARTIFACT_PATHS.items():
        if path.exists() and path.is_file():
            docs[key] = path.read_text(encoding="utf-8")
    return docs


def verify_continuity_artifacts() -> Dict[str, Any]:
    """Verify the canonical continuity artifacts exist and contain expected content."""
    docs = find_continuity_documents()
    missing: List[str] = []
    for key, path in ARTIFACT_PATHS.items():
        if key not in docs:
            missing.append(str(path))

    keywords = {
        "charter": ["living agnostic", "evidence before certainty", "human consent"],
        "continuity_pack": ["continue from the latest verified state", "preserve the living charter"],
    }

    keyword_checks: Dict[str, Dict[str, bool]] = {}
    for key, terms in keywords.items():
        content = docs.get(key, "").lower()
        keyword_checks[key] = {term: term in content for term in terms}

    return {
        "artifact_count": len(docs),
        "missing_artifacts": missing,
        "keyword_checks": keyword_checks,
    }


def continuity_summary() -> Dict[str, Any]:
    """Produce a simple continuity summary for the repository."""
    docs = find_continuity_documents()
    verification = verify_continuity_artifacts()
    return {
        "artifacts": sorted(docs.keys()),
        "artifact_count": verification["artifact_count"],
        "missing_artifacts": verification["missing_artifacts"],
        "keyword_checks": verification["keyword_checks"],
    }
