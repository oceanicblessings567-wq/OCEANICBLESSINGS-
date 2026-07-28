//! Rust Oceanic IR Adapter for executing and validating contracts.

use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct IrPayload {
    pub kind: String,
    pub intent: String,
    pub evidence: String,
    pub proof_required: bool,
    pub target: String,
    pub dissent_tokens: Vec<String>,
}

#[derive(Debug, Clone)]
pub struct AdapterResult {
    pub status: String,
    pub adapter: String,
    pub intent: String,
    pub evidence: String,
    pub verified_in_adapter: bool,
    pub error: Option<String>,
}

pub struct RustOceanicAdapter {
    pub context: HashMap<String, String>,
}

impl RustOceanicAdapter {
    pub fn new(context: HashMap<String, String>) -> Self {
        Self { context }
    }

    pub fn execute_ir(&self, ir: &IrPayload) -> Result<AdapterResult, String> {
        if ir.kind != "oceanic_ir" {
            return Err("Invalid IR payload: wrong kind".to_string());
        }

        let intent = ir.intent.trim();
        let evidence = ir.evidence.trim();

        if intent.is_empty() {
            return Err("Empty intent payload".to_string());
        }

        Ok(AdapterResult {
            status: "executed".to_string(),
            adapter: "rust".to_string(),
            intent: intent.to_string(),
            evidence: evidence.to_string(),
            verified_in_adapter: !evidence.is_empty(),
            error: None,
        })
    }
}
