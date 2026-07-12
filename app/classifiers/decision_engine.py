from app.classifiers.rule_classifier import RuleClassifier

from app.classifiers.hf_classifier import HFClassifier

from app.classifiers.gemini_classifier import GeminiClassifier

from app.services.parser.schemas import ParsedEmail
from app.classifiers.decision_trace import DecisionTrace
from app.classifiers.config import DecisionConfig


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
        print("Rule:", rule.category, rule.confidence)

        if rule.confidence >= DecisionConfig.RULE_ACCEPT:
            return DecisionTrace(rule=rule, hf=None, gemini=None, final=rule)

        # ---------------- HF ----------------

        hf = await self.hf.predict(email)
        print("HF:", hf.category, hf.confidence)

        if hf.confidence >= DecisionConfig.HF_ACCEPT:
            return DecisionTrace(rule=rule, hf=hf, gemini=None, final=hf)

        # ---------------- Gemini ----------------

        gemini = await self.gemini.predict(
            email=email,
            rule=rule,
            hf=hf,
        )

        return DecisionTrace(rule=rule, hf=hf, gemini=gemini, final=gemini)
