from app.classifiers.base import BaseClassifier


class GeminiClassifier(BaseClassifier):

    async def predict(
        self,
        email,
    ):

        raise NotImplementedError
