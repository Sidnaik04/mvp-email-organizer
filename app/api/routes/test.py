from fastapi import APIRouter

from app.database.models import User
from app.database.session import SessionLocal

from app.services.gmail.service import GmailService
from app.services.parser.email_parser import EmailParser

from app.core.rules.engine import RuleEngine
from app.classifiers.decision_engine import DecisionEngine

router = APIRouter(
    prefix="/test",
    tags=["Testing"],
)


@router.get("/rule-engine")
async def test_rule_engine():

    db = SessionLocal()

    try:

        user = db.query(User).first()

        if not user:
            return {"error": "No authenticated user found"}

        messages = GmailService.get_messages(
            user=user,
            max_results=20,
        )

        results = []

        for message in messages:

            raw_email = GmailService.get_message(
                user=user,
                message_id=message["id"],
            )

            parsed_email = EmailParser.parse(raw_email)

            print(parsed_email.sender_domain)

            engine = DecisionEngine()

            rule_result = engine.classify(parsed_email)

            results.append(
                {
                    "sender": parsed_email.sender,
                    "domain": parsed_email.sender_domain,
                    "subject": parsed_email.subject,
                    "category": rule_result.category,
                    "confidence": rule_result.confidence,
                    "reasons": rule_result.reasons,
                    "scores": rule_result.scores,
                }
            )

        return results

    finally:
        db.close()
