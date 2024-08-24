from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SignUpEventSchemaInput(BaseModel):
    Name: str
    Surname: str
    SignUpDate: datetime
    EventId: str
    Email: str
    PhoneNumber: str
    NumberOfGuests: int

    


class SignUpEventSchemaOutput(BaseModel):
    Status: str
    Id: int
    
    Name: str
    Surname: str
    SignUpDate: datetime
    EventId: str
    Email: str
    PhoneNumber: str
    NumberOfGuests: int