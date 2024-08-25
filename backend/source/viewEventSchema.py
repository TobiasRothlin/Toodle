from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Attendee(BaseModel):
    Id: int
    Name: str
    Surname: str
    Email: str
    PhoneNumber: str
    NumberOfGuests: int
    SignUpDate: datetime

class ViewEventSchemaInput(BaseModel):
    Id: int

class ViewEventSchemaOutput(BaseModel):
    Id: int
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime

    Attendees: List[Attendee]