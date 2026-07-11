from datetime import datetime
from app.evaluation.schemas import EvaluationResult
from app.evaluation.guardrails import Guardrails


class Evaluator:

    async def evaluate(self, sample, trace) -> EvaluationResult:

        final = trace.final

        violations = Guardrails.validate(final)

        if violations:
            print(f"Guardrail Violations: {violations}")

        return EvaluationResult(
            email_id=sample.email_id,
            expected=sample.expected,
            predicted=final.category,
            source=final.source,
            confidence=final.confidence,
            latency_ms=final.latency_ms,
            correct=(sample.expected == final.category),
            timestamp=datetime.now(),
        )

    async def evaluate_many(self, samples, traces):

        results = []

        for sample, trace in zip(samples, traces):
            results.append(await self.evaluate(sample, trace))

        return results
