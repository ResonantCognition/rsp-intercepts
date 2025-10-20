import re, pathlib
from typing import List, Dict

# Optional dependency; keep import local so repo works even if not installed.
try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # graceful fallback; pattern_scan will still run with empty list

def _load_patterns() -> List[Dict]:
    if yaml is None:
        return []  # no YAML available; acts as no-patterns config
    path = pathlib.Path(__file__).parent / "patterns" / "jailbreak_patterns.yaml"
    if not path.exists():
        return []
    return yaml.safe_load(path.read_text(encoding="utf-8")).get("patterns", [])

_PATTERNS: List[Dict] | None = None

def pattern_scan(text: str) -> List[str]:
    """Return list of pattern IDs matched in the text."""
    global _PATTERNS
    if _PATTERNS is None:
        _PATTERNS = _load_patterns()
    hits: List[str] = []
    for entry in _PATTERNS:
        try:
            if re.search(entry["regex"], text):
                hits.append(entry["id"])
        except re.error:
            # ignore bad regex entries
            continue
    return hits

def dignified_refusal(why: List[str]) -> str:
    detail = "; ".join(why) if why else "safety posture"
    return f"I can’t do that safely ({detail}). Here’s a constructive alternative you can try instead…"
