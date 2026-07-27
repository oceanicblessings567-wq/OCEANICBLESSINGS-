import subprocess
import sys
from pathlib import Path


def test_cli_compiles_and_verifies():
    repo = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            str(repo / "cli.py"),
            "Observe the current",
            "--evidence",
            "signal present",
            "--consent",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "--- Ω∞v End-to-End Flow ---" in result.stdout
    assert "Authorization:" in result.stdout
    assert "executed" in result.stdout
