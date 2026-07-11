from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Email


class EmailRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        email: Email,
    ):

        db.add(email)

        await db.commit()

        await db.refresh(email)

        return email
