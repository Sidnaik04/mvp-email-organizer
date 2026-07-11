from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True, nullable=False)

    name = Column(String)

    access_token = Column(Text)

    refresh_token = Column(Text)


class Email(Base):

    __tablename__ = "emails"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    gmail_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    thread_id: Mapped[str] = mapped_column(
        String(255),
    )

    sender: Mapped[str] = mapped_column(
        String(255),
    )

    domain: Mapped[str] = mapped_column(
        String(255),
    )

    subject: Mapped[str] = mapped_column(
        Text,
    )

    snippet: Mapped[str] = mapped_column(
        Text,
    )

    received_at: Mapped[datetime] = mapped_column(
        DateTime,
    )
