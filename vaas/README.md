# VaaS — Verification-as-a-Service

VaaS frames the Ω∞v ecosystem as an infrastructural and commercial offering focused on validated hesitation, proof-backed decision infrastructure, and trustworthy uncertainty.

## Core Positioning

- **Sell Validated Hesitation**: Hesitation before high-risk execution is not slowness; it is intelligence.
- **Proof-Backed Infrastructure**: Issue cryptographically verifiable proof tokens for all attested intents.
- **Legible Drift & Uncertainty**: Quantify mismatch between planned models and runtime observations.

## Live Endpoints

- `POST /api/vaas/verify`: Submit intent and evidence to receive hesitation index, posture, drift audit, and proof token.
- `GET /api/vaas/proof`: Query the proof token registry.

## API Payload Example

```json
{
  "intent": "Execute high-value transaction",
  "evidence": "multisig log hash 0x7f8a...",
  "target": "python"
}
```

## Response Schema

```json
{
  "ir": { "kind": "oceanic_ir", "intent": "...", "target": "python" },
  "verification": { "verified": true, "confidence": 0.95 },
  "hesitation": { "hesitation_score": 0.05, "posture": "proceed" },
  "proof_token": { "token_id": "proof_a1b2c3d4e5f67890", "proof_hash": "..." },
  "drift_audit": { "drift_detected": false, "status": "in_alignment" },
  "status": "success"
}
```

## Module Reference

The underlying VaaS logic is powered by `omega.vaas`:
- `calculate_hesitation_score(ir, verification)`
- `issue_proof_token(ir, verification, attestation)`
- `audit_drift(ir, observation)`
