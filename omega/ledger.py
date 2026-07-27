"""Ledger for Ω∞v event history."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict


def record_event(event_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Create a ledger entry for an event."""
    return {
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "payload": payload,
    }
