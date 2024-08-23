from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CreateEventSchemaInput(BaseModel):
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime
    RequiredInformation: List[str]
    OptionalInformation: List[str]


class CreateEventSchemaOutput(BaseModel):
    Name: str
    Description: str
    MaxAttendees: int
    Date: datetime
    SineUpDeadline: datetime
    RequiredInformation: List[str]
    OptionalInformation: List[str]
    Id: str
