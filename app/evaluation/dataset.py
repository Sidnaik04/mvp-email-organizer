import json
from pathlib import Path

from app.core.rules.categories import Category
from app.evaluation.schemas import EvaluationSample
from app.services.parser.schemas import ParsedEmail


class DatasetLoader:

    @staticmethod
    def load(path: str) -> list[EvaluationSample]:

        file = Path(path)

        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)

        samples = []

        for item in data:

            samples.append(
                EvaluationSample(
                    email_id=item["email_id"],
                    expected=Category(item["expected"]),
                    email=ParsedEmail(
                        sender=item["sender"],
                        sender_domain=item["domain"],
                        subject=item["subject"],
                        snippet=item["snippet"],
                    ),
                )
            )

        return samples
