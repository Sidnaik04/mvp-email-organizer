from app.classifiers.base import BaseClassifier


class HFClassifier(BaseClassifier):

    def predict(
        self,
        email,
    ):

        raise NotImplementedError
