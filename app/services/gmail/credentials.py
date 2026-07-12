from google.oauth2.credentials import Credentials

from app.database.models import User
from app.config.settings import get_settings

settings = get_settings()


def get_credentials(user: User):

    return Credentials(
        token=user.access_token,
        refresh_token=user.refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=settings.google_client_id,
        client_secret=settings.google_client_secret,
    )
