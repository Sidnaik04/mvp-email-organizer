from app.classifiers.base import BaseClassifier
from app.services.huggingface.client import HFClient
from app.classifiers.result import ClassificationResult
from time import perf_counter
from app.core.rules.categories import Category


class HFClassifier(BaseClassifier):

    def __init__(self):
        self.client = HFClient()

        self.labels = [c.value for c in Category if c != Category.UNKNOWN]

    async def predict(
        self,
        email,
    ):

        context = BaseClassifier.build_email_context(email)

        start = perf_counter()

        response = await self.client.classify(context, self.labels)

        end = perf_counter()

        best = response[0]["label"]

        confidence = response[0]["score"]

        category = Category(best)

        scores = {item["label"]: item["score"] for item in response}

        return ClassificationResult(
            source="hf",
            category=category,
            confidence=confidence,
            reasons=["ModernBERT Zero Shot"],
            scores=scores,
            latency_ms=(end - start) * 1000,
        )
