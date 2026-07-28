import json
import subprocess
import sys
import time
from pathlib import Path


def wait_for_server(port=8000, max_attempts=10):
    import socket
    for _ in range(max_attempts):
        try:
            with socket.create_connection(("localhost", port), timeout=1):
                return
        except OSError:
            time.sleep(0.2)
    raise RuntimeError("Server did not start in time")


def test_web_full_stack_flow():
    repo = Path(__file__).resolve().parents[1]
    proc = subprocess.Popen(
        [sys.executable, str(repo / "web/server.py")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        import urllib.request

        wait_for_server()
        url = "http://localhost:8000/api/run"
        payload = {
            "intent": "Observe the system",
            "evidence": "signal present",
            "target": "python",
            "consent": True,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")

        result = json.loads(body)
        assert result["authorization"]["authorized"] is True
        assert result["execution"]["executed"] is True
        assert "target_code" in result["ir"]
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def test_web_vaas_verify_endpoint():
    repo = Path(__file__).resolve().parents[1]
    proc = subprocess.Popen(
        [sys.executable, str(repo / "web/server.py")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        import urllib.request

        wait_for_server()
        url = "http://localhost:8000/api/vaas/verify"
        payload = {
            "intent": "Verify secure operation",
            "evidence": "log trace 99",
            "target": "javascript",
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")

        result = json.loads(body)
        assert result["status"] == "success"
        assert "hesitation" in result
        assert "proof_token" in result
        assert result["proof_token"]["token_id"].startswith("proof_")
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
        import urllib.request

        wait_for_server()
        url = "http://localhost:8000/api/continuity"

        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")

        result = json.loads(body)
        assert result["artifact_count"] >= 4
        assert "charter" in result["artifacts"]
        assert "continuity_pack" in result["artifacts"]
    finally:
        proc.terminate()
        proc.wait(timeout=5)
