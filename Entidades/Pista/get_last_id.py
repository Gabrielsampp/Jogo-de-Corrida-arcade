
import json
from pathlib import Path

path = Path(__file__).parent / "pista.json"

def get_last_id():
    file = open(path, "r", encoding="utf-8")

    data = json.load(file)

    try:
        return data["tracks"][-1]["id"]

    except:
        return 0