from app.core.rules.domains import DOMAIN_RULES


class DomainMatcher:

    @staticmethod
    def score(email, board):
        domain = email.sender_domain.lower()

        matched = None

        # find the longest matching suffix
        for rule_domain in DOMAIN_RULES:

            if domain == rule_domain or domain.endswith(f".{rule_domain}"):
                # prefer the most specific match
                if matched is None or len(rule_domain) > len(matched):
                    macthed = rule_domain

        if matched:

            rule = DOMAIN_RULES[matched]

            board.add(
                category=rule["category"],
                weight=rule["weight"],
                reason=f"Matched domain '{matched}'",
                high_precision=True,
            )
