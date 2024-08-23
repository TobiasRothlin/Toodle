from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ViewEventSchemaInput(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None

class ViewEventSchemaOutput(BaseModel):
    Id: str
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime
    RequiredInformation: List[str]
    OptionalInformation: List[str]
    Attendees: List[str]