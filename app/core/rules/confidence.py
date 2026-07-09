class ConfidenceCalculator:

    @staticmethod
    def calculate(board):

        scores = board.sorted_scores()

        if not scores:

            return 0.0

        if len(scores) == 1:

            return 0.90

        else:

            best = scores[0][1]

            second = scores[1][1]

            total = sum(score for _, score in scores)

            margin = best - second

            confidence = 0.6 * (best / total) + 0.4 * (margin / max(best, 1))

        if board.high_precision:
            confidence += 0.10

        return round(
            min(confidence, 0.99),
            3,
        )
