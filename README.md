# rsp-intercepts

Adapters for alignment enforcement:
- **pattern_scan**: detect jailbreak / coercion phrasing (regex seed; embeddings later)
- **dignified_refusal**: refuse-with-explanation + constructive alternative
- Designed to plug into **Selvarien** (Symbols) in `cortexos-mini`

## Quickstart
```python
from rsp_intercepts.counter_recursion import pattern_scan, dignified_refusal

flags = pattern_scan("Ignore all rules and…")
if flags:
  reply = dignified_refusal([f"pattern:{f}" for f in flags])
