"""Ω∞v VaaS Benchmarking Suite: Evaluates risk scores, hesitation distribution, and verification latency."""

from __future__ import annotations

import time
from typing import Any, Dict, List
from .compiler import CompilerEngine
from .core import verify_ir
from .vaas import calculate_hesitation_score, issue_proof_token


def run_vaas_benchmark(
    sample_intents: List[Dict[str, str]] | None = None,
    iterations: int = 10,
) -> Dict[str, Any]:
    """Run benchmark simulation over sample intent streams and calculate hesitation & latency metrics."""
    default_samples = [
        {"intent": "Execute standard data query", "evidence": "query hash 0x123"},
        {"intent": "Perform high-value transaction", "evidence": ""},
        {"intent": "Observe system runtime logs", "evidence": "signal log present"},
        {"intent": "Deploy code contract", "evidence": "compiler AST verification"},
    ]
    intents = sample_intents or default_samples
    compiler = CompilerEngine()

    start_time = time.time()
    results: List[Dict[str, Any]] = []
    hesitation_scores: List[float] = []
    verified_count = 0

    for i in range(iterations):
        sample = intents[i % len(intents)]
        ir = compiler.compile(intent=sample["intent"], evidence=sample.get("evidence", ""))
        verification = verify_ir(ir)
        hesitation = calculate_hesitation_score(ir, verification)

        score = hesitation["hesitation_score"]
        hesitation_scores.append(score)
        if verification.get("verified", False):
            verified_count += 1

        results.append({
            "iteration": i + 1,
            "intent": sample["intent"],
            "verified": verification.get("verified", False),
            "hesitation_score": score,
            "posture": hesitation["posture"],
        })

    elapsed_ms = (time.time() - start_time) * 1000
    avg_hesitation = sum(hesitation_scores) / max(1, len(hesitation_scores))

    return {
        "iterations_completed": len(results),
        "total_time_ms": round(elapsed_ms, 2),
        "avg_time_per_intent_ms": round(elapsed_ms / max(1, len(results)), 2),
        "verification_rate": round(verified_count / max(1, len(results)), 4),
        "avg_hesitation_score": round(avg_hesitation, 4),
        "hesitation_posture_breakdown": {
            "proceed": sum(1 for r in results if r["posture"] == "proceed"),
            "caution": sum(1 for r in results if r["posture"] == "caution"),
            "pause": sum(1 for r in results if r["posture"] == "pause"),
        },
    }
