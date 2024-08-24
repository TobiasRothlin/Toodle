from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    id: int
    name: str
    description: str
    max_attendees: int
    date: datetime
    sign_up_deadline: datetime
    show_number_of_guests: bool
    is_mail_required: bool
    is_phone_number_required: bool

