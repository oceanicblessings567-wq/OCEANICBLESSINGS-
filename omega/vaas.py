"""Verification-as-a-Service (VaaS) core logic for Ω∞v.

Provides proof-backed decision infrastructure, validated hesitation scoring,
proof token generation, and drift auditing.
"""

from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Dict


def calculate_hesitation_score(
    ir: Dict[str, Any],
    verification: Dict[str, Any],
) -> Dict[str, Any]:
    """Calculate the hesitation score and risk posture for a given IR & verification result.

    Hesitation reflects justified uncertainty before authorization.
    Higher hesitation indicates low confidence or missing evidence.
    """
    verified = verification.get("verified", False)
    confidence = verification.get("confidence", 0.0)
    has_evidence = bool(ir.get("evidence", "").strip())
    dissent_tokens = ir.get("dissent_tokens", [])

    base_hesitation = 1.0 - confidence
    if not has_evidence:
        base_hesitation += 0.3
    if dissent_tokens:
        base_hesitation += len(dissent_tokens) * 0.1

    hesitation_score = min(1.0, max(0.0, base_hesitation))
    posture = "proceed" if hesitation_score < 0.3 else ("caution" if hesitation_score < 0.7 else "pause")

    return {
        "hesitation_score": round(hesitation_score, 4),
        "posture": posture,
        "verified": verified,
        "factors": {
            "missing_evidence": not has_evidence,
            "confidence": confidence,
            "dissent_token_count": len(dissent_tokens),
        },
    }


def issue_proof_token(
    ir: Dict[str, Any],
    verification: Dict[str, Any],
    attestation: Dict[str, Any],
) -> Dict[str, Any]:
    """Generate a verifiable proof token for an attested Oceanic IR contract."""
    timestamp = int(time.time())
    payload = {
        "intent": ir.get("intent", ""),
        "evidence": ir.get("evidence", ""),
        "verified": verification.get("verified", False),
        "trust_level": attestation.get("trust_level", "low"),
        "timestamp": timestamp,
    }
    serialized = json.dumps(payload, sort_keys=True).encode("utf-8")
    proof_hash = hashlib.sha256(serialized).hexdigest()

    return {
        "token_id": f"proof_{proof_hash[:16]}",
        "proof_hash": proof_hash,
        "issued_at": timestamp,
        "payload": payload,
        "status": "valid" if verification.get("verified", False) else "unverified_proof",
    }


def audit_drift(
    ir: Dict[str, Any],
    observation: Dict[str, Any],
) -> Dict[str, Any]:
    """Audit drift between planned intent and actual observation."""
    expected = ir.get("intent", "")
    observed_match = observation.get("match", False)

    drift_detected = not observed_match
    drift_score = 0.0 if observed_match else 0.85

    return {
        "drift_detected": drift_detected,
        "drift_score": drift_score,
        "expected_intent": expected,
        "observed_output": observation.get("output", ""),
        "status": "in_alignment" if not drift_detected else "drift_warning",
    }
