from app.classifiers.rule_classifier import RuleClassifier

from app.classifiers.hf_classifier import HFClassifier

from app.classifiers.gemini_classifier import GeminiClassifier

from app.services.parser.schemas import ParsedEmail
from app.classifiers.decision_trace import DecisionTrace
from app.classifiers.config import DecisionConfig
from app.config.logging import logger


class DecisionEngine:

    def __init__(self):

        self.rule = RuleClassifier()
        self.hf = HFClassifier()
        self.gemini = GeminiClassifier()

    async def classify(
        self,
        email: ParsedEmail,
    ) -> DecisionTrace:

        # ---------------- Rule ----------------

        rule = await self.rule.predict(email)
        logger.info(f"Rule: {rule.category} ({rule.confidence:.2f})")

        if rule.confidence >= DecisionConfig.RULE_ACCEPT:
            return DecisionTrace(
                rule=rule,
                hf=None,
                gemini=None,
                final=rule,
                decision_source="rule",
                model="rule-engine-v1",
            )

        # ---------------- HF ----------------

        hf = await self.hf.predict(email)
        logger.info(f"HF: {hf.category} ({hf.confidence:.2f})")

        if hf.confidence >= DecisionConfig.HF_ACCEPT:
            return DecisionTrace(
                rule=rule,
                hf=hf,
                gemini=None,
                final=hf,
                decision_source="hf",
                model="ModernBERT-large-zeroshot-v2.0",
            )

        # ---------------- Gemini ----------------

        gemini = await self.gemini.predict(
            email=email,
            rule=rule,
            hf=hf,
        )

        return DecisionTrace(
            rule=rule,
            hf=hf,
            gemini=gemini,
            final=gemini,
            decision_source="gemini",
            model="gemini-2.5-flash",
        )
