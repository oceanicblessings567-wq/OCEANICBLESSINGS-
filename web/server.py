from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from omega import (
    compile_intent,
    verify_ir,
    attest,
    authorize,
    execute,
    observe,
    record_event,
    continuity_summary,
)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/":
            self.serve_file("index.html", "text/html")
            return

        if self.path == "/api/continuity":
            self.send_json(continuity_summary())
            return

        if self.path.endswith(".js"):
            self.serve_file(self.path.lstrip("/"), "application/javascript")
            return

        self.send_error(404, "Not Found")

    def send_json(self, body: dict) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body, indent=2).encode("utf-8"))

    def do_POST(self) -> None:
        if self.path != "/api/run":
            self.send_error(404, "Not Found")
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        payload = json.loads(body.decode("utf-8"))

        ir = compile_intent(payload.get("intent", ""), evidence=payload.get("evidence", ""))
        verification = verify_ir(ir)
        attestation = attest(ir, verification)
        authorization = authorize(attestation, consent=payload.get("consent", False))
        execution = execute(ir, authorization)
        observation = observe(execution, ir)

        events = [
            record_event("intent_compiled", ir),
            record_event("verification_completed", verification),
            record_event("attestation_created", attestation),
            record_event("authorization_result", authorization),
            record_event("execution_result", execution),
            record_event("observation_result", observation),
        ]

        response = {
            "ir": ir,
            "verification": verification,
            "attestation": attestation,
            "authorization": authorization,
            "execution": execution,
            "observation": observation,
            "ledger": events,
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))

    def serve_file(self, filename: str, content_type: str) -> None:
        root = Path(__file__).resolve().parent
        path = root / filename
        if not path.exists():
            self.send_error(404, "Not Found")
            return

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(path.read_bytes())


def run(server_class=HTTPServer, handler_class=Handler, port=8000) -> None:
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting Ω∞v full-stack server at http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
