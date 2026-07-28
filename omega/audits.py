"""Drift analysis and audit logging for Ω∞v."""

from __future__ import annotations

from typing import Any, Dict, List


def run_drift_audit(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Perform audit scan over ledger events to calculate cumulative system drift."""
    total_events = len(events)
    unauthorized_count = 0
    diverged_count = 0

    for event in events:
        payload = event.get("payload", {})
        if event.get("event_type") == "authorization_result" and not payload.get("authorized", True):
            unauthorized_count += 1
        elif event.get("event_type") == "observation_result" and not payload.get("match", True):
            diverged_count += 1

    drift_index = round((unauthorized_count + diverged_count) / max(1, total_events), 4)

    return {
        "total_events_audited": total_events,
        "unauthorized_attempts": unauthorized_count,
        "diverged_observations": diverged_count,
        "cumulative_drift_index": drift_index,
        "audit_pass": drift_index < 0.3,
        "recommendation": "Maintain state" if drift_index < 0.3 else "Trigger evolution cycle",
    }
