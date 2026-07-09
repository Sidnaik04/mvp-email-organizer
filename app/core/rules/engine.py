from app.core.rules.scoring import ScoreBoard
from app.core.rules.keyword_matcher import KeywordMatcher
from app.core.rules.domain_matcher import DomainMatcher
from app.core.rules.sender_matcher import SenderMatcher
from app.core.rules.confidence import ConfidenceCalculator
from app.core.rules.result import RuleResult
from app.core.rules.categories import Category


class RuleEngine:

    @staticmethod
    def classify(email):

        board = ScoreBoard()

        DomainMatcher.score(email, board)

        SenderMatcher.score(email, board)

        KeywordMatcher.score_text(
            email.sender_name or "",
            "Sender",
            board,
            multiplier=3,
        )

        KeywordMatcher.score_text(
            email.subject,
            "Subject",
            board,
            multiplier=2,
        )

        KeywordMatcher.score_text(
            email.snippet,
            "Snippet",
            board,
            multiplier=1,
        )

        category = board.best_category()

        if category is None:

            return RuleResult(
                category=Category.UNKNOWN,
                confidence=0.0,
                reasons=["No rules macthed"],
                scores={},
            )

        confidence = ConfidenceCalculator.calculate(board)

        return RuleResult(
            category=category,
            confidence=confidence,
            reasons=board.reasons.get(category, []),
            scores={c.value: s for c, s in board.scores.items()},
        )
