from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.crud import EmailRepository
from app.database.db import get_db
from app.database.models import Email

router = APIRouter(
    prefix="/database",
    tags=["Database"],
)


@router.get("/test")
async def test_database(
    db: AsyncSession = Depends(get_db),
):

    email = Email(
        gmail_id="test_gmail_id",
        thread_id="test_thread",
        sender="test@example.com",
        domain="example.com",
        subject="Hello",
        snippet="Testing SQLite",
        received_at=datetime.utcnow(),
    )

    created = await EmailRepository.create(
        db=db,
        email=email,
    )

    return created
