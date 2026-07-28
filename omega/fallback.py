"""Fallback and local-first resilience module for Ω∞v."""

from __future__ import annotations

from typing import Any, Dict


def fallback_execution(
    ir: Dict[str, Any],
    reason: str = "degraded_environment",
) -> Dict[str, Any]:
    """Provide local-first, safe fallback execution when primary pipeline is degraded."""
    intent = ir.get("intent", "<unknown>")
    
    return {
        "executed": True,
        "mode": "fallback_local_first",
        "reason": reason,
        "output": f"[FALLBACK RUNTIME] Safe local execution of intent: '{intent}'",
        "trust_posture": "local_verification_only",
        "error": None,
    }
