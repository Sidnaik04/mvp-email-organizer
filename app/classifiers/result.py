from pydantic import BaseModel

from app.core.rules.categories import Category


class ClassificationResult(BaseModel):

    source: str

    category: Category

    confidence: float

    reasons: list[str]

    scores: dict[str, float]
