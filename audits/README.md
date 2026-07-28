# Ω∞v Audits & Drift Analysis

The Audits module scans recorded system events to detect mismatch between models and reality, maintaining system alignment and precision over time.

## Drift Index Calculation

The cumulative drift index evaluates unauthorized execution attempts and diverged observations across all recorded ledger events:

$$\text{Drift Index} = \frac{\text{Unauthorized Attempts} + \text{Diverged Observations}}{\max(1, \text{Total Ledger Events})}$$

## Programmatic API (`omega.audits`)

```python
from omega import run_drift_audit

events = [
    {"event_type": "authorization_result", "payload": {"authorized": True}},
    {"event_type": "observation_result", "payload": {"match": False}},
]

audit_result = run_drift_audit(events)
# {"total_events_audited": 2, "cumulative_drift_index": 0.5, "audit_pass": false}
```

## REST API Endpoint

- `GET /api/audit`: Returns drift index, event statistics, and evolution recommendation.
