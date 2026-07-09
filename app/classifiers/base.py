from abc import ABC
from abc import abstractmethod

from app.services.parser.schemas import ParsedEmail

from app.classifiers.result import ClassificationResult


class BaseClassifier(ABC):

    @abstractmethod
    def predict(
        self,
        email: ParsedEmail,
    ) -> ClassificationResult: ...
