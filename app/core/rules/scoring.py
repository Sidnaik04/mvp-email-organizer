from collections import defaultdict

from app.core.rules.categories import Category


class ScoreBoard:

    def __init__(self):

        self.scores = defaultdict(float)
        self.reasons = defaultdict(list)
        self.high_precision = False

    def add(self, category, weight, reason, high_precision=False):
        self.scores[category] += weight

        self.reasons[category].append(reason)

        if high_precision:
            self.high_precision = True

    def best_category(self):
        if not self.scores:
            return None

        return max(
            self.scores,
            key=self.scores.get,
        )

    def sorted_scores(self):
        return sorted(
            self.scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

    def get_score(self, category):
        return self.scores[category]
