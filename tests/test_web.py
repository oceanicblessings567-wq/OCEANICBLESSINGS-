import json
import subprocess
import sys
import time
from pathlib import Path


def test_web_full_stack_flow():
    repo = Path(__file__).resolve().parents[1]
    proc = subprocess.Popen(
        [sys.executable, str(repo / "web/server.py")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        import socket
        import urllib.request

        url = "http://localhost:8000/api/run"
        payload = {
            "intent": "Observe the system",
            "evidence": "signal present",
            "consent": True,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        for _ in range(10):
            try:
                with socket.create_connection(("localhost", 8000), timeout=1):
                    break
            except OSError:
                time.sleep(0.2)
        else:
            raise RuntimeError("Server did not start in time")

        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")

        result = json.loads(body)
        assert result["authorization"]["authorized"] is True
        assert result["execution"]["executed"] is True
        assert result["observation"]["match"] is False or result["observation"]["match"] is True
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def test_web_continuity_endpoint():
    repo = Path(__file__).resolve().parents[1]
    proc = subprocess.Popen(
        [sys.executable, str(repo / "web/server.py")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        import socket
        import urllib.request

        url = "http://localhost:8000/api/continuity"
        for _ in range(10):
            try:
                with socket.create_connection(("localhost", 8000), timeout=1):
                    break
            except OSError:
                time.sleep(0.2)
        else:
            raise RuntimeError("Server did not start in time")

        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")

        result = json.loads(body)
        assert result["artifact_count"] >= 4
        assert "charter" in result["artifacts"]
        assert "continuity_pack" in result["artifacts"]
    finally:
        proc.terminate()
        proc.wait(timeout=5)
