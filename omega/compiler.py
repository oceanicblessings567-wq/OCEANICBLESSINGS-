"""Ω∞v Compiler Engine: Translates human intent into Oceanic IR and target code snippets."""

from __future__ import annotations

import json
from typing import Any, Dict, List
from .ir import build_ir, validate_ir


class CompilerEngine:
    """Multi-pass compiler translating human intent into verified Oceanic IR contracts."""

    def __init__(self, default_target: str = "python") -> None:
        self.default_target = default_target

    def compile(
        self,
        intent: str,
        evidence: str | None = None,
        target: str | None = None,
        dissent_tokens: List[str] | None = None,
    ) -> Dict[str, Any]:
        """Compile raw intent through analysis, dissent injection, and IR generation passes."""
        target_lang = target or self.default_target
        
        # Pass 1: Extract intent & auto-detect dissent signals
        detected_dissent = dissent_tokens or []
        if not evidence and "unverified" not in detected_dissent:
            detected_dissent.append("missing_evidence_warning")

        # Pass 2: Build IR AST representation
        ir = build_ir(
            intent=intent,
            evidence=evidence,
            target=target_lang,
            dissent_tokens=detected_dissent,
        )

        if not validate_ir(ir):
            raise ValueError("Compilation error: Generated IR failed validation invariants.")

        # Pass 3: Generate executable code artifact for target language
        target_code = self.generate_target_code(ir)
        ir["target_code"] = target_code

        return ir

    def generate_target_code(self, ir: Dict[str, Any]) -> str:
        """Generate target language code block from compiled IR."""
        target = ir.get("target", "python").lower()
        intent = ir.get("intent", "")
        evidence = ir.get("evidence", "")

        if target in ("js", "javascript", "node"):
            return (
                "// Oceanic IR Contract (JavaScript Target)\n"
                f"const intent = {json.dumps(intent)};\n"
                f"const evidence = {json.dumps(evidence)};\n"
                "function executeContract() {\n"
                "  if (!intent) throw new Error('Empty intent');\n"
                "  return { status: 'executed', intent, evidence, timestamp: new Date().toISOString() };\n"
                "}\n"
                "module.exports = { executeContract };"
            )
        elif target in ("sh", "shell", "bash"):
            return (
                "#!/usr/bin/env bash\n"
                "# Oceanic IR Contract (Shell Target)\n"
                f'INTENT="{intent}"\n'
                f'EVIDENCE="{evidence}"\n'
                'echo "[Ω∞v RUNTIME] Executing intent: $INTENT"\n'
            )
        else:
            # Default to Python target
            return (
                "# Oceanic IR Contract (Python Target)\n"
                f"INTENT = {json.dumps(intent)}\n"
                f"EVIDENCE = {json.dumps(evidence)}\n\n"
                "def execute_contract():\n"
                "    if not INTENT:\n"
                "        raise ValueError('Empty intent')\n"
                "    return {'status': 'executed', 'intent': INTENT, 'evidence': EVIDENCE}\n"
            )
