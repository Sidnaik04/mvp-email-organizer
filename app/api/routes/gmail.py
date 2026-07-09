from fastapi import APIRouter

from app.database.models import User
from app.database.session import SessionLocal
from app.services.gmail.service import GmailService
from app.services.parser.email_parser import EmailParser

router = APIRouter(prefix="/gmail", tags=["Gmail"])


@router.get("/messages")
async def messages():

    db = SessionLocal()

    user = db.query(User).first()

    messages = GmailService.get_messages(user=user, max_results=10)

    result = []

    for message in messages:

        email = GmailService.get_message(user=user, message_id=message["id"])

        parsed = EmailParser.parse(email)

        result.append(parsed.model_dump())

    db.close()

    return result
