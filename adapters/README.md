# Ω∞v Universal Adapters

Adapters connect the neutral Oceanic IR contract layer to specific target programming languages and execution environments.

## Available Adapters

### 1. Python Adapter ([adapters/python/oceanic_adapter.py](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/python/oceanic_adapter.py))
```python
from adapters.python.oceanic_adapter import PythonOceanicAdapter

adapter = PythonOceanicAdapter()
result = adapter.execute_ir(ir_payload)
```

### 2. JavaScript / Node.js Adapter ([adapters/js/oceanic_adapter.js](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/js/oceanic_adapter.js))
```javascript
const { JavaScriptOceanicAdapter } = require('./adapters/js/oceanic_adapter');

const adapter = new JavaScriptOceanicAdapter();
const result = adapter.executeIr(irPayload);
```
