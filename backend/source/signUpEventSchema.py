from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SignUpEventSchemaInput(BaseModel):
    Name: str
    Id: str
    


class SignUpEventSchemaOutput(BaseModel):
    Status: str
    Name: str
    Id: str