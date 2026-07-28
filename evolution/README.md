# Ω∞v Evolution Engine

Evolution is the loop that turns evidence into systemic posture adaptation. It observes outcomes, measures divergence, proposes posture adjustments, and applies approved changes.

## Evolution Cycle

$$\text{Observe} \rightarrow \text{Learn} \rightarrow \text{Propose} \rightarrow \text{Verify} \rightarrow \text{Evolve}$$

## Programmatic API (`omega.evolution`)

```python
from omega import propose_evolution, apply_evolution

observation = {"match": False, "output": "Execution diverged"}
drift = {"drift_score": 0.85}

# 1. Propose posture evolution
proposal = propose_evolution(observation, drift)

# 2. Apply proposal
result = apply_evolution(proposal)
print(result) # {"applied": True, "status": "evolved", ...}
```
