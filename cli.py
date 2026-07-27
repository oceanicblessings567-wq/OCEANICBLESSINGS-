from __future__ import annotations

import argparse

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


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Ω∞v end-to-end flow.")
    parser.add_argument("intent", nargs="?", help="Human intent to compile and execute")
    parser.add_argument("--evidence", default="", help="Evidence supporting the intent")
    parser.add_argument("--consent", action="store_true", help="Simulate human consent for authorization")
    parser.add_argument("--continuity", action="store_true", help="Show continuity summary and exit")
    args = parser.parse_args()

    if args.continuity:
        summary = continuity_summary()
        print(json.dumps(summary, indent=2))
        return

    if not args.intent:
        parser.error("the following arguments are required: intent")

    ir = compile_intent(args.intent, evidence=args.evidence)
    verification = verify_ir(ir)
    attestation = attest(ir, verification)
    authorization = authorize(attestation, consent=args.consent)
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

    print("--- Ω∞v End-to-End Flow ---")
    print("Intent:", args.intent)
    print("Evidence:", args.evidence)
    print("IR:", ir)
    print("Verification:", verification)
    print("Attestation:", attestation)
    print("Authorization:", authorization)
    print("Execution:", execution)
    print("Observation:", observation)
    print("Ledger events:")
    for event in events:
        print(event)


if __name__ == "__main__":
    main()
