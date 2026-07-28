// Package oceanicprovides Go Oceanic IR contract execution adapter.
package oceanic

import (
	"errors"
	"strings"
	"time"
)

// IrPayload represents a canonical Oceanic IR payload in Go.
type IrPayload struct {
	Kind          string   `json:"kind"`
	Intent        string   `json:"intent"`
	Evidence      string   `json:"evidence"`
	ProofRequired bool     `json:"proof_required"`
	Target        string   `json:"target"`
	DissentTokens []string `json:"dissent_tokens"`
}

// AdapterResult represents the execution outcome of an IR contract.
type AdapterResult struct {
	Status            string    `json:"status"`
	Adapter           string    `json:"adapter"`
	Intent            string    `json:"intent,omitempty"`
	Evidence          string    `json:"evidence,omitempty"`
	VerifiedInAdapter bool      `json:"verified_in_adapter"`
	Timestamp         time.Time `json:"timestamp"`
	Error             string    `json:"error,omitempty"`
}

// GoOceanicAdapter executes Oceanic IR payloads within Go environments.
type GoOceanicAdapter struct {
	Context map[string]interface{}
}

// NewGoOceanicAdapter initializes a new Go adapter.
func NewGoOceanicAdapter(ctx map[string]interface{}) *GoOceanicAdapter {
	if ctx == nil {
		ctx = make(map[string]interface{})
	}
	return &GoOceanicAdapter{Context: ctx}
}

// ExecuteIR validates and executes an Oceanic IR payload.
func (a *GoOceanicAdapter) ExecuteIR(ir IrPayload) (AdapterResult, error) {
	if ir.Kind != "oceanic_ir" {
		return AdapterResult{Status: "error", Adapter: "go", Error: "invalid IR payload kind"}, errors.New("invalid IR payload kind")
	}

	intent := strings.TrimSpace(ir.Intent)
	evidence := strings.TrimSpace(ir.Evidence)

	if intent == "" {
		return AdapterResult{Status: "rejected", Adapter: "go", Error: "empty intent payload"}, errors.New("empty intent payload")
	}

	return AdapterResult{
		Status:            "executed",
		Adapter:           "go",
		Intent:            intent,
		Evidence:          evidence,
		VerifiedInAdapter: evidence != "",
		Timestamp:         time.Now().UTC(),
	}, nil
}
