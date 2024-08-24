from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CreateEventSchemaInput(BaseModel):
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime
    showNumberOfGuests: bool
    isMailRequired: bool
    isPhoneNumberRequired: bool
    


class CreateEventSchemaOutput(BaseModel):
    Id: int
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime
    showNumberOfGuests: bool
    isMailRequired: bool
    isPhoneNumberRequired: bool
    