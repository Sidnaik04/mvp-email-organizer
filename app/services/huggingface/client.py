import logging
from huggingface_hub import AsyncInferenceClient
from app.config.settings import get_settings

settings = get_settings()

logger = logging.getLogger(__name__)


class HFClient:

    def __init__(self):
        self.client = AsyncInferenceClient(
            model="facebook/bart-large-mnli",
            token=settings.hf_api_key,
            timeout=60.0,
        )

    async def classify(self, text: str, labels: list[str]):

        if not text.strip():
            raise ValueError("Email text cannot be empty")
        if len(labels) < 2:
            raise ValueError("At least 2 labels are required for classification")

        try:
            result = await self.client.zero_shot_classification(
                text=text, candidate_labels=labels, multi_label=False
            )

            return result

        except Exception as e:
            logger.error(f"HF Zero-Shot Classification Error: {str(e)}")
            raise
