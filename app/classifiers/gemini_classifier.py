from app.classifiers.base import BaseClassifier
from app.classifiers.result import ClassificationResult

from app.services.gemini.client import GeminiClient
from app.services.gemini.prompt import build_prompt


class GeminiClassifier(BaseClassifier):

    def __init__(self):
        self.client = GeminiClient()

    async def predict(
        self,
        email,
        rule,
        hf,
    ):

        prompt = build_prompt(email, rule, hf)

        result = await self.client.classify(prompt)

        return ClassificationResult(
            source="gemini",
            category=result.category,
            confidence=result.confidence,
            reasons=[result.reason],
            scores={},
        )
