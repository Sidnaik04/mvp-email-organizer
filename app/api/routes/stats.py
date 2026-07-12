import json
from collections import Counter
from pathlib import Path
from fastapi import APIRouter

router = APIRouter(prefix="/stats", tags=["statistics"])

LOG_FILE = Path("data/classification_history.jsonl")


@router.get("")
async def stats():

    if not LOG_FILE.exists():
        return {}

    category_counter = Counter()
    source_counter = Counter()
    model_counter = Counter()

    total = 0
    confidence_sum = 0

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            record = json.loads(line)

            total += 1

            # be defensive: older records may not have `final`, `model`, or `decision_source`
            final = record.get("final") or {}
            category = final.get("category", "unknown")
            confidence = final.get("confidence", 0)

            category_counter[category] += 1
            confidence_sum += confidence

            model = record.get("model", "unknown")
            model_counter[model] += 1

            decision_source = record.get("decision_source", record.get("final", {}).get("source", "unknown"))
            source_counter[decision_source] += 1

    average_confidence = round(confidence_sum / total, 2) if total else 0

    return {
        "total_processed": total,
        "average_confidence": average_confidence,
        "categories": dict(category_counter),
        "models": dict(model_counter),
        "decision_source": dict(source_counter),
    }
