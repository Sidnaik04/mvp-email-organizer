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

    def build_email_context(email):
        return f"""
    Sender: {email.sender_name}
    Domain: {email.sender_domain}

    Subject:
    {email.subject}

    Snippet:
    {email.snippet}
    """
