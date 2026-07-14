from fastapi import APIRouter

from app.database.models import User
from app.database.session import SessionLocal

from app.services.gmail.service import GmailService
from app.services.parser.email_parser import EmailParser

from app.core.rules.engine import RuleEngine
from app.classifiers.decision_engine import DecisionEngine
from app.services.logger.classification_logger import ClassificationLogger
from app.services.gmail.label_service import GmailLabelService
from app.config.logging import logger

import time

router = APIRouter(
    prefix="/classify",
    tags=["Classify"],
)


@router.post("/inbox")
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

        existing_ids = ClassificationLogger.load_existing_ids()

        results = []

        processed = 0
        skipped = 0
        duration_ms = 0.0

        for message in messages:

            start = time.perf_counter()

            if message["id"] in existing_ids:

                skipped += 1

                continue

            raw_email = GmailService.get_message(
                user=user,
                message_id=message["id"],
            )

            parsed_email = EmailParser.parse(raw_email)

            logger.info(f"Sender domain: {parsed_email.sender_domain}")

            engine = DecisionEngine()

            trace = await engine.classify(parsed_email)

            ClassificationLogger.log(
                gmail_id=message["id"], parsed_email=parsed_email, trace=trace
            )

            existing_ids.add(message["id"])

            processed += 1

            GmailLabelService.label_email(
                user=user, message_id=message["id"], category=trace.final.category
            )

            end = time.perf_counter()

            results.append(
                {
                    "sender": parsed_email.sender,
                    "domain": parsed_email.sender_domain,
                    "subject": parsed_email.subject,
                    "category": trace.final.category,
                    "confidence": trace.final.confidence,
                    "reasons": trace.final.reasons,
                    "scores": trace.final.scores,
                    "rule": trace.rule,
                    "hf": trace.hf,
                    "gemini": trace.gemini,
                    "final": trace.final,
                }
            )

            duration_ms = round((end - start) * 1000, 2)

        return {
            "processed": processed,
            "skipped": skipped,
            "duration_ms": duration_ms,
            "results": results,
        }

    finally:
        db.close()
