import json
from pathlib import Path

DATA_DIR = Path("data/ao_sections")

def load_ao_section(filename: str):
    file_path = DATA_DIR / filename

    if not file_path.exists():
        return {"error": f"File {filename} not found"}

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
