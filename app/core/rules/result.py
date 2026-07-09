from pydantic import BaseModel

from app.core.rules.categories import Category


class RuleResult(BaseModel):

    category: Category

    confidence: float

    reasons: list[str]

    scores: dict[Category, float]
