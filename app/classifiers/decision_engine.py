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

    def classify(self, email: ParsedEmail) -> ClassificationResult:
        
        # rule
        rule = self.rule.predict(email)
        
        if rule.confidence >= DecisionConfig.RULE_ACCEPT:
            
            return rule
        
        # HF
        hf = self.hf.predict(email)
        
        return hf
