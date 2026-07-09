from google import genai

from app.config.settings import get_settings
from app.services.gemini.schemas import GeminiResponse

settings = get_settings()


class GeminiClient:

    def __init__(self):

        self.client = genai.Client(api_key=settings.google_genai_api_key)

    async def classify(self, prompt):

        response = await self.client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": GeminiResponse,
                "temperature": 0.1,
            },
        )

        return response.parsed
