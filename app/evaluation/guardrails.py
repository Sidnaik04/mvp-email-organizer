from app.classifiers.result import ClassificationResult
from app.core.rules.categories import Category


class Guardrails:

    @staticmethod
    def validate(result: ClassificationResult) -> list[str]:

        violations = []

        if result.category not in Category:

            violations.append("Invalid category")

        if not (0.0 <= result.confidence <= 1.0):
            violations.append("Confidence out of range")

        if not result.reasons:
            violations.append("Reason Missing")

        return violations
