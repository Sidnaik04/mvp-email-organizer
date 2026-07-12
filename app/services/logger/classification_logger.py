import json
from datetime import datetime, UTC
from pathlib import Path

LOG_FILE = Path("data/classification_history.jsonl")


class ClassificationLogger:

    @staticmethod
    def log(gmail_id: str, parsed_email, trace):
        record = {
            "timestamp": datetime.now(UTC).isoformat(),
            "gmail_id": gmail_id,
            "sender": parsed_email.sender,
            "domain": parsed_email.sender_domain,
            "subject": parsed_email.subject,
            "snippet": parsed_email.snippet,
            "rule": trace.rule.model_dump() if trace.rule else None,
            "hf": trace.hf.model_dump() if trace.hf else None,
            "gemini": trace.gemini.model_dump() if trace.gemini else None,
            "final": trace.final.model_dump(),
        }

        with open(LOG_FILE, "a", encoding="utf8") as f:

            f.write(json.dumps(record, ensure_ascii=False) + "\n")


    @staticmethod
    def load_existing_ids() -> set[str]:

        if not LOG_FILE.exists():
            return set()

        ids = set()

        with open(LOG_FILE, "r", encoding="utf-8") as f:

            for line in f:

                try:

                    record = json.loads(line)

                    ids.add(record["gmail_id"])

                except json.JSONDecodeError:
                    continue

        return ids 