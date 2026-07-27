"""Minimal Ω∞v core for compiling intent into Oceanic IR and verifying it."""

from __future__ import annotations

from typing import Any, Dict

from .ir import build_ir, validate_ir


def compile_intent(intent: str, evidence: str | None = None) -> Dict[str, Any]:
    """Transform a human intent into a canonical Oceanic IR structure."""
    ir = build_ir(intent, evidence=evidence)
    if not validate_ir(ir):
        raise ValueError("Compiled IR is invalid")
    return ir


def verify_ir(ir: Dict[str, Any]) -> Dict[str, Any]:
    """Verify that the IR contains enough information for trust."""
    has_intent = bool(ir.get("intent", "").strip())
    has_evidence = bool(ir.get("evidence", "").strip())
    has_proof = bool(ir.get("proof_required", False))

    verified = has_intent and has_evidence and has_proof
    confidence = 0.95 if verified else 0.3

    return {
        "verified": verified,
        "status": "verified" if verified else "needs_more_evidence",
        "confidence": confidence,
    }
