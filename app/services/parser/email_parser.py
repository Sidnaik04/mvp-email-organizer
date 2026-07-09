from email.utils import parseaddr

from app.services.parser.schemas import ParsedEmail


class EmailParser:

    @staticmethod
    def parse(message: dict) -> ParsedEmail:

        headers = {
            h["name"]: h["value"]
            for h in message["payload"]["headers"]
        }

        sender = headers.get("From", "")

        sender_name, sender_email = parseaddr(sender)

        domain = ""

        if "@" in sender_email:
            domain = sender_email.split("@")[1].lower()

        return ParsedEmail(
            message_id=message["id"],
            thread_id=message["threadId"],

            sender=sender_email,
            sender_name=sender_name or None,
            sender_domain=domain,

            subject=headers.get("Subject", ""),

            snippet=message.get("snippet", ""),

            date=headers.get("Date", ""),
        )