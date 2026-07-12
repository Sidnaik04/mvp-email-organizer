from sqlalchemy.orm import Session
from app.database.models import Email, ClassificationTrace, DatasetCandidate


class EmailRepository:

    @staticmethod
    def get_by_gmail_id(db: Session, gmail_id: str):
        return db.query(Email).filter(Email.gmail_id == gmail_id).first()

    @staticmethod
    def create(
        db: Session,
        **kwargs,
    ):

        email = Email(**kwargs)

        db.add(email)
        db.commit()
        db.refresh(email)

        return email

    @staticmethod
    def mark_processed(db: Session, email: Email):
        email.processed = True

        db.commit()
        db.refresh(email)

        return email


class TraceRepository:

    @staticmethod
    def create(
        db: Session,
        **kwargs,
    ):

        trace = ClassificationTrace(**kwargs)

        db.add(trace)

        db.commit()

        db.refresh(trace)

        return trace


class DatasetRepository:

    @staticmethod
    def create(
        db: Session,
        **kwargs,
    ):

        candidate = DatasetCandidate(**kwargs)

        db.add(candidate)

        db.commit()

        db.refresh(candidate)

        return candidate
