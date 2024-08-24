from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Attendee(BaseModel):
    Name: str
    Surname: str
    Email: str
    PhoneNumber: str
    NumberOfGuests: int
    SignUpDate: datetime

class ViewEventSchemaInput(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class ViewEventSchemaOutput(BaseModel):
    Id: int
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime
    showNumberOfGuests: bool
    isMailRequired: bool
    isPhoneNumberRequired: bool
    Attendees: List[Attendee]