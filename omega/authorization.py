"""Authorization layer for Ω∞v decisions."""

from __future__ import annotations

from typing import Any, Dict


def authorize(attestation: Dict[str, Any], consent: bool = True) -> Dict[str, Any]:
    """Authorize execution based on attestation and consent."""
    authorized = attestation.get("attested", False) and bool(consent)
    return {
        "authorized": authorized,
        "consent": bool(consent),
        "reason": "authorized" if authorized else "denied",
    }
