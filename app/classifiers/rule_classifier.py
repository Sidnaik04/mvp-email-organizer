from app.classifiers.base import BaseClassifier
from app.classifiers.result import ClassificationResult

from app.core.rules.engine import RuleEngine


class RuleClassifier(BaseClassifier):

    async def predict(
        self,
        email,
    ) -> ClassificationResult:

        result = RuleEngine.classify(email)

        return ClassificationResult(
            source="rule",
            category=result.category,
            confidence=result.confidence,
            reasons=result.reasons,
            scores=result.scores,
        )
