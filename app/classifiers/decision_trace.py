from pydantic import BaseModel

from app.classifiers.result import ClassificationResult


class DecisionTrace(BaseModel):

    rule: ClassificationResult | None

    hf: ClassificationResult | None

    gemini: ClassificationResult | None

    final: ClassificationResult
