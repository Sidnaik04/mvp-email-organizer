from app.classifiers.base import BaseClassifier
from app.classifiers.result import ClassificationResult
from time import perf_counter

from app.core.rules.engine import RuleEngine


class RuleClassifier(BaseClassifier):

    async def predict(
        self,
        email,
    ) -> ClassificationResult:

        start = perf_counter()

        result = RuleEngine.classify(email)

        end = perf_counter()

        return ClassificationResult(
            source="rule",
            category=result.category,
            confidence=result.confidence,
            reasons=result.reasons,
            scores=result.scores,
            latency_ms=(end - start) * 1000,
        )
