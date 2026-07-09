from app.database.models import User
from app.services.gmail.gmail_client import GmailClient


class GmailService:

    @staticmethod
    def get_messages(user: User, max_results: int = 10):

        service = GmailClient.get_service(user)

        response = (
            service.users()
            .messages()
            .list(
                userId="me",
                maxResults=max_results,
            )
            .execute()
        )

        return response.get("messages", [])

    @staticmethod
    def get_message(user: User, message_id: str):

        service = GmailClient.get_service(user)

        return (
            service.users()
            .messages()
            .get(
                userId="me",
                id=message_id,
                format="metadata",
                metadataHeaders=["Subject", "From", "Date"],
            )
            .execute()
        )
