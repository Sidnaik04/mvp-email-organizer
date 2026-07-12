from authlib.integrations.starlette_client import OAuth

from app.config.settings import get_settings

settings = get_settings()

oauth = OAuth()

SCOPES = [
    "openid",
    "email",
    "profile",
    "https://www.googleapis.com/auth/gmail.modify",
]

oauth.register(
    name="google",
    client_id=settings.google_client_id,
    client_secret=settings.google_client_secret,
    server_metadata_url=(
        "https://accounts.google.com/.well-known/openid-configuration"
    ),
    client_kwargs={"scope": " ".join(SCOPES)},
)
