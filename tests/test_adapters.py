from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from adapters.python.oceanic_adapter import PythonOceanicAdapter
from omega import build_ir


def test_python_oceanic_adapter():
    ir = build_ir("Execute verified query", evidence="log_hash_999")
    adapter = PythonOceanicAdapter()
    result = adapter.execute_ir(ir)

    assert result["status"] == "executed"
    assert result["adapter"] == "python"
    assert result["intent"] == "Execute verified query"
    assert result["verified_in_adapter"] is True


def test_python_oceanic_adapter_rejects_empty_intent():
    ir = {"kind": "oceanic_ir", "intent": "", "evidence": ""}
    adapter = PythonOceanicAdapter()
    result = adapter.execute_ir(ir)

    assert result["status"] == "rejected"
    assert "Empty intent payload" in result["reason"]


def test_python_oceanic_adapter_validates_kind():
    ir = {"kind": "invalid_kind", "intent": "Some intent"}
    adapter = PythonOceanicAdapter()
    result = adapter.execute_ir(ir)

    assert result["status"] == "error"
    assert "wrong kind" in result["message"]
