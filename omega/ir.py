"""Oceanic IR schema helpers and validation rules."""

from __future__ import annotations

from typing import Any, Dict, List


def build_ir(
    intent: str,
    evidence: str | None = None,
    target: str = "python",
    dissent_tokens: List[str] | None = None,
) -> Dict[str, Any]:
    """Build a canonical Oceanic IR structure from intent, evidence, and optional parameters."""
    clean_intent = intent.strip()
    clean_evidence = (evidence or "").strip()
    dissent = dissent_tokens or []

    return {
        "kind": "oceanic_ir",
        "intent": clean_intent,
        "evidence": clean_evidence,
        "proof_required": True,
        "target": target,
        "dissent_tokens": dissent,
        "metadata": {
            "source": "omega.compiler",
            "version": "0.1.0",
        },
    }


def validate_ir(ir: Dict[str, Any]) -> bool:
    """Validate an Oceanic IR payload against structural invariants."""
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

    if "target" in ir and not isinstance(ir.get("target"), str):
        return False

    if "dissent_tokens" in ir and not isinstance(ir.get("dissent_tokens"), list):
        return False

    return True
