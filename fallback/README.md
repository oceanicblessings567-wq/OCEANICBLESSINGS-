# Ω∞v Fallback & Local-First Resilience

Fallback ensures system availability under partial infrastructure failure or degraded network connectivity. It favors local-first execution, graceful degradation, and legibility.

## Features

- **Local-First Execution**: Continues local evaluation when remote verification endpoints are unreachable.
- **Graceful Degradation**: Relies on safe local invariants rather than halting operations.

## Programmatic API (`omega.fallback`)

```python
from omega import build_ir, fallback_execution

ir = build_ir("Process offline task", evidence="local buffer")
fallback_res = fallback_execution(ir, reason="network_unreachable")

# {"executed": True, "mode": "fallback_local_first", ...}
```

## REST API Endpoint

- `POST /api/fallback`: Accepts intent payload and executes local fallback pipeline.
