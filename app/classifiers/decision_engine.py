from app.classifiers.rule_classifier import RuleClassifier

from app.classifiers.hf_classifier import HFClassifier

from app.classifiers.gemini_classifier import GeminiClassifier

from app.services.parser.schemas import ParsedEmail
from app.classifiers.result import ClassificationResult

from app.classifiers.config import DecisionConfig


class DecisionEngine:

    def __init__(self):

        self.rule = RuleClassifier()
        self.hf = HFClassifier()
        self.gemini = GeminiClassifier()

    async def classify(self, email: ParsedEmail) -> ClassificationResult:

        # rule
        rule = await self.rule.predict(email)

        print("Rule:", rule.category, rule.confidence)

        if rule.confidence >= DecisionConfig.RULE_ACCEPT:

            return rule

        # HF
        hf = await self.hf.predict(email)

        print("HF:", hf.category, hf.confidence)

        if (
            hf.category == rule.category
            and hf.confidence >= DecisionConfig.HF_AGREEMENT
        ):
            return hf

        if hf.confidence >= DecisionConfig.HF_ACCEPT:
            return hf

        if hf.confidence > rule.confidence:
            return hf

        if hf.confidence < DecisionConfig.HF_MINIMUM:
            return rule

        return hf

        # gemini

        # return await self.gemini.predict(email)
