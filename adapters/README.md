# Ω∞v Universal Adapters

Adapters connect the neutral Oceanic IR contract layer to specific target programming languages and execution environments.

## Available Adapters

### 1. Python Adapter ([adapters/python/oceanic_adapter.py](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/python/oceanic_adapter.py))
```python
from adapters.python.oceanic_adapter import PythonOceanicAdapter

adapter = PythonOceanicAdapter()
result = adapter.execute_ir(ir_payload)
```

### 2. JavaScript Adapter ([adapters/js/oceanic_adapter.js](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/js/oceanic_adapter.js))
```javascript
const { JavaScriptOceanicAdapter } = require('./adapters/js/oceanic_adapter');

const adapter = new JavaScriptOceanicAdapter();
const result = adapter.executeIr(irPayload);
```

### 3. TypeScript Adapter ([adapters/ts/oceanic_adapter.ts](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/ts/oceanic_adapter.ts))
```typescript
import { TypeScriptOceanicAdapter } from './adapters/ts/oceanic_adapter';

const adapter = new TypeScriptOceanicAdapter();
const result = adapter.executeIr(irPayload);
```

### 4. Go Adapter ([adapters/go/oceanic_adapter.go](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/go/oceanic_adapter.go))
```go
import "oceanic"

adapter := oceanic.NewGoOceanicAdapter(nil)
result, err := adapter.ExecuteIR(irPayload)
```

### 5. Rust Adapter ([adapters/rust/oceanic_adapter.rs](file:///c:/Users/pc/OCEANICBLESSINGS-/adapters/rust/oceanic_adapter.rs))
```rust
use rust_adapter::{RustOceanicAdapter, IrPayload};

let adapter = RustOceanicAdapter::new(HashMap::new());
let result = adapter.execute_ir(&ir_payload);
```
