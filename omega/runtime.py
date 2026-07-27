"""Runtime execution for Ω∞v intents."""

from __future__ import annotations

from typing import Any, Dict


def execute(ir: Dict[str, Any], authorization: Dict[str, Any]) -> Dict[str, Any]:
    """Execute the verified intent when authorized."""
    if not authorization.get("authorized", False):
        return {
            "executed": False,
            "output": None,
            "error": "execution not authorized",
        }

    output = f"Executed intent: {ir.get('intent', '<unknown>')}"
    return {
        "executed": True,
        "output": output,
        "error": None,
    }
