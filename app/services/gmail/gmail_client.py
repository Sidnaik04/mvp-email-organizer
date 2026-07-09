from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

from app.database.models import User
from app.config.settings import get_settings

settings = get_settings()


class GmailClient:

    @staticmethod
    def get_service(user: User):

        credentials = Credentials(
            token=user.access_token,
            refresh_token=user.refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=settings.google_client_id,
            client_secret=settings.google_client_secret,
        )

        service = build("gmail", "v1", credentials=credentials, cache_discovery=False)

        return service
