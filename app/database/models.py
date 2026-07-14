from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base
from datetime import datetime, UTC


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True, nullable=False)

    name = Column(String)

    access_token = Column(Text)

    refresh_token = Column(Text)


class Email(Base):

    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)

    gmail_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    thread_id = Column(String)

    sender = Column(String)

    sender_domain = Column(String)

    subject = Column(Text)

    snippet = Column(Text)

    received_at = Column(DateTime)

    processed = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.now(UTC),
    )


class ClassificationTrace(Base):

    __tablename__ = "classification_traces"

    id = Column(Integer, primary_key=True)

    email_id = Column(
        Integer,
        ForeignKey("emails.id"),
        nullable=False,
    )

    rule_category = Column(String)

    rule_confidence = Column(Float)

    hf_category = Column(String)

    hf_confidence = Column(Float)

    gemini_category = Column(String)

    gemini_confidence = Column(Float)

    final_category = Column(String)

    decision_source = Column(String)

    latency_ms = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.now(),
    )


class DatasetCandidate(Base):

    __tablename__ = "dataset_candidates"

    id = Column(Integer, primary_key=True)

    email_id = Column(
        Integer,
        ForeignKey("emails.id"),
        nullable=False,
    )

    label = Column(String)

    confidence = Column(Float)

    status = Column(
        String,
        default="PENDING",
    )

    verified = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )