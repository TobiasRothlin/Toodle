from pydantic import BaseModel
from datetime import datetime

class SignUp(BaseModel):
    id: int
    name: str
    surname: str
    sign_up_date: datetime
    event_id: int

    email: str
    phone_number: str
    number_of_guests: int
    
