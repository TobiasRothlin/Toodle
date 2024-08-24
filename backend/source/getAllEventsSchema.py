from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SingleEvent(BaseModel):
    Id: int
    Name: str    

class GetAllEventsSchemaOutput(BaseModel):
    Events: List[SingleEvent]