from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Google OAuth
    google_client_id: str = Field(..., alias="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(..., alias="GOOGLE_CLIENT_SECRET")
    google_redirect_uri: str = Field(..., alias="GOOGLE_REDIRECT_URI")

    # Gemini
    google_genai_api_key: str = Field(..., alias="GOOGLE_GENAI_API_KEY")

    # HuggingFace
    hf_api_key: str = Field(..., alias="HF_API_KEY")

    # Database
    database_url: str = Field(..., alias="DATABASE_URL")

    # Logging
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")


# ensures .env file is loaded only once during application startup
@lru_cache
def get_settings() -> Settings:
    return Settings()
