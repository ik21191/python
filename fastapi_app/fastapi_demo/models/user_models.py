from pydantic import BaseModel, Field, EmailStr
#EmailStr is used for email validation
#Field is used for field validation
from typing import Optional

class SignupDetails(BaseModel):
    first_name:str 
    last_name: Optional[str] = None
    email:EmailStr
    password:str
    mobile:int
    age:int = Field(ge=18, le=100)