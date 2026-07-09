from pydantic import BaseModel, Field

from app.core.rules.categories import Category


class GeminiResponse(BaseModel):

    category: Category

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    reason: str