from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from omega import CompilerEngine, validate_ir


def test_compiler_engine_python_target():
    compiler = CompilerEngine()
    ir = compiler.compile("Run data sync", evidence="db connection active", target="python")

    assert validate_ir(ir)
    assert ir["target"] == "python"
    assert "def execute_contract" in ir["target_code"]


def test_compiler_engine_javascript_target():
    compiler = CompilerEngine()
    ir = compiler.compile("Process web task", evidence="session token", target="javascript")

    assert validate_ir(ir)
    assert ir["target"] == "javascript"
    assert "executeContract" in ir["target_code"]


def test_compiler_engine_shell_target():
    compiler = CompilerEngine()
    ir = compiler.compile("Backup server", evidence="disk space ok", target="shell")

    assert validate_ir(ir)
    assert ir["target"] == "shell"
    assert "#!/usr/bin/env bash" in ir["target_code"]
