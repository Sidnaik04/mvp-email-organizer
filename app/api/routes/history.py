import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter(prefix="/history", tags=["History"])

LOG_FILE = Path("data/classification_history.jsonl")


@router.get("")
async def history(limit: int = 50):

    if not LOG_FILE.exists():
        return []

    records = []

    with open(LOG_FILE, "r", encoding="utf-8") as f:

        for line in f:
            records.append(json.loads(line))

    return records[-limit:][::-1]
