from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    organization_id: Optional[int]

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True
