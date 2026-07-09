from app.core.rules.sender_rules import SENDER_RULES


class SenderMatcher:

    @staticmethod
    def score(email, board):

        sender = (email.sender_name or "").lower()

        for key, category in SENDER_RULES.items():

            if key in sender:

                board.add(
                    category,
                    30,
                    f"Sender matched '{key}'",
                    high_precision=True,
                )