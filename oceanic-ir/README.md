# Oceanic IR (Intermediate Representation) Specification

Oceanic IR is the language-agnostic schema defining verified form within the Ω∞v ecosystem.

## Canonical Schema

```json
{
  "kind": "oceanic_ir",
  "intent": "Declared human intent string",
  "evidence": "Supporting evidence, logs, or hash",
  "proof_required": true,
  "target": "python | javascript | shell",
  "dissent_tokens": ["missing_evidence_warning"],
  "metadata": {
    "source": "omega.compiler",
    "version": "0.1.0"
  }
}
```

## Structural Invariants

1. `kind` MUST strictly equal `"oceanic_ir"`.
2. `intent` MUST be a non-null string.
3. `evidence` MUST be a string representation (may be empty if unverified).
4. `proof_required` MUST be boolean `true`.
