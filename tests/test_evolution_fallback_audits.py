from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from omega import (
    build_ir,
    propose_evolution,
    apply_evolution,
    fallback_execution,
    run_drift_audit,
)


def test_propose_and_apply_evolution():
    observation = {"match": False, "output": "execution diverged"}
    drift = {"drift_score": 0.8}

    proposal = propose_evolution(observation, drift)
    assert proposal["needs_evolution"] is True
    assert proposal["proposal_id"].startswith("evo_")

    result = apply_evolution(proposal)
    assert result["applied"] is True
    assert result["status"] == "evolved"


def test_fallback_execution():
    ir = build_ir("Process offline task", evidence="local buffer")
    result = fallback_execution(ir, reason="network_unreachable")

    assert result["executed"] is True
    assert result["mode"] == "fallback_local_first"
    assert "FALLBACK RUNTIME" in result["output"]


def test_run_drift_audit():
    events = [
        {"event_type": "authorization_result", "payload": {"authorized": True}},
        {"event_type": "observation_result", "payload": {"match": True}},
        {"event_type": "observation_result", "payload": {"match": False}},
    ]
    audit = run_drift_audit(events)

    assert audit["total_events_audited"] == 3
    assert audit["diverged_observations"] == 1
    assert "cumulative_drift_index" in audit
