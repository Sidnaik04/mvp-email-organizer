from datetime import datetime

from pydantic import BaseModel

from app.classifiers.decision_trace import DecisionTrace
from app.core.rules.categories import Category
from app.services.parser.schemas import ParsedEmail

class EvaluationSample(BaseModel):
    """
    One labeled email in the evaluation dataset.
    """

    email_id: str
    
    email: ParsedEmail

    expected: Category


class EvaluationResult(BaseModel):
    """
    Result after evaluating one email.
    """

    email_id: str

    expected: Category

    predicted: Category

    source: str

    confidence: float

    latency_ms: float

    correct: bool

    timestamp: datetime


class EvaluationSummary(BaseModel):

    total: int

    correct: int

    accuracy: float

    avg_latency_ms: float

    avg_confidence: float
