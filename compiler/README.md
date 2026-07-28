# Ω∞v Compiler Module

The compiler is the translation bridge from human intent into neutral Oceanic IR, and subsequently into target-specific executable code contracts.

## Multi-Pass Architecture

1. **Intent Analysis & Dissent Extraction**: Evaluates incoming human prompt and detects missing evidence or dissent signals.
2. **IR AST Generation**: Synthesizes canonical `oceanic_ir` payloads with target bindings and verification metadata.
3. **Target Code Generation**: Produces executable contract code for target runtimes:
   - **Python Target**: Python function contracts (`def execute_contract()`).
   - **JavaScript / Node.js Target**: CommonJS / ES module contracts (`executeContract()`).
   - **Shell / Bash Target**: Executable bash script contracts.

## Code Example

```python
from omega import CompilerEngine

compiler = CompilerEngine()
ir = compiler.compile(
    intent="Observe network traffic",
    evidence="pcap log present",
    target="javascript",
)

print(ir["target_code"])
```
