"""Oceanic IR schema helpers."""

from __future__ import annotations

from typing import Any, Dict


def build_ir(intent: str, evidence: str | None = None) -> Dict[str, Any]:
    """Build a canonical Oceanic IR structure from intent and evidence."""
    return {
        "kind": "oceanic_ir",
        "intent": intent.strip(),
        "evidence": (evidence or "").strip(),
        "proof_required": True,
        "metadata": {
            "source": "omega.compiler",
        },
    }


def validate_ir(ir: Dict[str, Any]) -> bool:
    """Validate a simple Oceanic IR payload."""
    if not isinstance(ir, dict):
        return False

    required_keys = {"kind", "intent", "evidence", "proof_required"}
    if not required_keys.issubset(ir.keys()):
        return False

    if ir.get("kind") != "oceanic_ir":
        return False

    if not isinstance(ir.get("intent"), str):
        return False

    if not isinstance(ir.get("evidence"), str):
        return False

    return True
