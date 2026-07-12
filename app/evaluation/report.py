from app.evaluation.metrics import Metrics
from app.evaluation.schemas import EvaluationResult, EvaluationSummary


class ReportGenerator:

    @staticmethod
    def generate(results: list[EvaluationResult]) -> EvaluationSummary:

        total = len(results)

        correct = sum(r.correct for r in results)

        return EvaluationSummary(
            total=total,
            correct=correct,
            accuracy=Metrics.accuracy(results),
            avg_latency_ms=Metrics.average_latency(results),
            avg_confidence=Metrics.average_confidence(results),
        )
