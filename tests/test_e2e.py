import subprocess
import sys
from pathlib import Path


def test_end_to_end_cli_flow():
    repo = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            str(repo / "cli.py"),
            "Run the Ω∞v flow",
            "--evidence",
            "sample evidence",
            "--consent",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "--- Ω∞v End-to-End Flow ---" in result.stdout
    assert "Authorization:" in result.stdout
    assert "executed" in result.stdout
    assert "match" in result.stdout
