import json
from pathlib import Path

def read_records(path):
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("records"), list):
        raise ValueError("资料必须包含 records 数组")
    return value["records"]
