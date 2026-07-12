import json
from pathlib import Path

INPUT_FILE = Path("data/classification_history.jsonl")
OUTPUT_FILE = Path("data/candidate_dataset.jsonl")

MIN_CONFIDENCE = 0.90


def main():

    total = 0
    accepted = 0

    with (
        open(INPUT_FILE, "r", encoding="utf-8") as infile,
        open(OUTPUT_FILE, "w", encoding="utf-8") as outfile,
    ):

        for line in infile:

            total += 1

            record = json.loads(line)

            final = record["final"]

            confidence = final["confidence"]

            if confidence < MIN_CONFIDENCE or final["category"] == "Unknown":
                continue

            dataset_record = {
                "gmail_id": record["gmail_id"],
                "sender": record["sender"],
                "domain": record["domain"],
                "subject": record["subject"],
                "snippet": record["snippet"],
                "label": final["category"],
                "confidence": final["confidence"],
                "source": record["final"].get("source"),
            }

            outfile.write(json.dumps(dataset_record) + "\n")

            accepted += 1

    print("=" * 40)
    print(f"Total Emails      : {total}")
    print(f"Accepted Samples  : {accepted}")
    print(f"Rejected Samples  : {total - accepted}")
    print("=" * 40)


if __name__ == "__main__":
    main()
