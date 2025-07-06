from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True
