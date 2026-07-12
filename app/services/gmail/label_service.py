from googleapiclient.discovery import build

from app.database.models import User
from app.services.gmail.credentials import get_credentials

CATEGORY_LABELS = [
    "Job Opening",
    "Software",
    "Technical Blogs",
    "Marketing",
    "Bank Statements",
    "Fitness",
    "Personal",
    "Programming",
]


class GmailLabelService:
    @staticmethod
    def _service(user: User):
        credentials = get_credentials(user)

        return build(
            "gmail",
            "v1",
            credentials=credentials,
            cache_discovery=False,
        )

    @staticmethod
    def get_or_create_label(
        user: User,
        label_name: str,
    ) -> str:

        service = GmailLabelService._service(user)

        labels = service.users().labels().list(userId="me").execute()

        for label in labels.get("labels", []):

            if label["type"] != "user":
                continue

            if label["name"].lower() == label_name.lower():
                return label["id"]

        new_label = (
            service.users()
            .labels()
            .create(
                userId="me",
                body={
                    "name": label_name,
                    "labelListVisibility": "labelShow",
                    "messageListVisibility": "show",
                },
            )
            .execute()
        )

        return new_label["id"]

    @staticmethod
    def apply_label(
        user: User,
        message_id: str,
        label_id: str,
    ):

        service = GmailLabelService._service(user)

        service.users().messages().modify(
            userId="me",
            id=message_id,
            body={
                "addLabelIds": [label_id],
            },
        ).execute()

    @staticmethod
    def label_email(
        user: User,
        message_id: str,
        category: str,
    ):

        GmailLabelService.remove_existing_category_labels(
            user=user, message_id=message_id
        )

        label_id = GmailLabelService.get_or_create_label(
            user=user,
            label_name=category,
        )

        GmailLabelService.apply_label(
            user=user,
            message_id=message_id,
            label_id=label_id,
        )

    @staticmethod
    def remove_existing_category_labels(
        user: User,
        message_id: str,
    ):

        service = GmailLabelService._service(user)

        labels = service.users().labels().list(userId="me").execute()

        category_label_ids = []

        for label in labels.get("labels", []):

            if label["type"] != "user":
                continue

            if label["name"] in CATEGORY_LABELS:
                category_label_ids.append(label["id"])

        if not category_label_ids:
            return

        service.users().messages().modify(
            userId="me",
            id=message_id,
            body={
                "removeLabelIds": category_label_ids,
            },
        ).execute()
