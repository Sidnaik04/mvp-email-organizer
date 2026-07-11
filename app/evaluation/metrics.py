from statistics import mean
from app.evaluation.schemas import EvaluationResult
from collections import Counter


class Metrics:

    @staticmethod
    def accuracy(
        results: list[EvaluationResult],
    ) -> float:

        if not results:
            return 0.0

        correct = sum(r.correct for r in results)

        return correct / len(results)

    @staticmethod
    def average_latency(results: list[EvaluationResult]) -> float:

        if not results:
            return 0.0

        return mean(r.latency_ms for r in results)

    @staticmethod
    def average_confidence(results: list[EvaluationResult]):
        if not results:
            return 0.0

        return mean(r.confidence for r in results)

    @staticmethod
    def routing_distribution(results):
        counts = Counter(r.source for r in results)

        return dict(counts)
