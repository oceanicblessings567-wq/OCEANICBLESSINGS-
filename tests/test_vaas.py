from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from omega import (
    build_ir,
    verify_ir,
    attest,
    calculate_hesitation_score,
    issue_proof_token,
    audit_drift,
    run_vaas_benchmark,
)


def test_calculate_hesitation_score():
    ir = build_ir("Verify system security", evidence="audit log present")
    verification = verify_ir(ir)
    hesitation = calculate_hesitation_score(ir, verification)

    assert "hesitation_score" in hesitation
    assert hesitation["posture"] in ("proceed", "caution", "pause")
    assert hesitation["verified"] is True


def test_issue_proof_token():
    ir = build_ir("Verify transaction", evidence="tx_hash_123")
    verification = verify_ir(ir)
    attestation = attest(ir, verification)
    proof = issue_proof_token(ir, verification, attestation)

    assert proof["status"] == "valid"
    assert proof["token_id"].startswith("proof_")
    assert len(proof["proof_hash"]) == 64


def test_audit_drift():
    ir = build_ir("Observe network", evidence="pings ok")
    observation = {"match": True, "output": "Observe network matched"}
    drift = audit_drift(ir, observation)

    assert drift["drift_detected"] is False
    assert drift["status"] == "in_alignment"


def test_run_vaas_benchmark():
    benchmark = run_vaas_benchmark(iterations=5)

    assert benchmark["iterations_completed"] == 5
    assert "avg_hesitation_score" in benchmark
    assert "hesitation_posture_breakdown" in benchmark
