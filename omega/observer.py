"""Observation layer for Ω∞v runtime outcomes."""

from __future__ import annotations

from typing import Any, Dict


def observe(execution: Dict[str, Any], ir: Dict[str, Any]) -> Dict[str, Any]:
    """Observe the execution result and compare it to expectations."""
    executed = execution.get("executed", False)
    output = execution.get("output", "") or ""
    expected_phrase = ir.get("intent", "")
    match = expected_phrase in output if expected_phrase else executed

    return {
        "observed": executed,
        "output": output,
        "match": match,
        "notes": "execution matched intent" if match else "execution diverged from intent",
    }
