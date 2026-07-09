from pydantic import BaseModel
from typing import Optional


class ParsedEmail(BaseModel):
    message_id: str
    thread_id: str

    sender: str
    sender_name: Optional[str]
    sender_domain: str

    subject: str
    snippet: str

    date: str
