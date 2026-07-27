from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from omega import compile_intent, verify_ir


def test_compile_intent_returns_oceanic_ir():
    ir = compile_intent("Observe the system", evidence="runtime log")

    assert ir["kind"] == "oceanic_ir"
    assert ir["intent"] == "Observe the system"
    assert ir["evidence"] == "runtime log"
    assert ir["proof_required"] is True


def test_verify_ir_returns_confidence_and_status():
    ir = {
        "kind": "oceanic_ir",
        "intent": "Verify the signal",
        "evidence": "matching output",
        "proof_required": True,
    }

    result = verify_ir(ir)

    assert result["verified"] is True
    assert result["status"] == "verified"
    assert result["confidence"] >= 0.8
