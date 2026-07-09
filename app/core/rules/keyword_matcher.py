from app.core.rules.keywords import KEYWORD_RULES
import re


import re

from app.core.rules.keywords import KEYWORD_RULES


class KeywordMatcher:

    @staticmethod
    def score_text(
        text: str,
        source: str,
        board,
        multiplier: float = 1.0,
    ):

        if not text:
            return

        text = text.lower()

        for category, keywords in KEYWORD_RULES.items():

            for keyword, weight in keywords.items():

                pattern = rf"\b{re.escape(keyword.lower())}\b"

                if re.search(pattern, text):

                    board.add(
                        category=category,
                        weight=weight * multiplier,
                        reason=f"{source}: '{keyword}'",
                    )
