from pydantic import BaseModel
from datetime import date

class ChargeBase(BaseModel):
    studentId: int
    studentName: str
    dueDate: date
    amount: float
    status: str

class ChargeCreate(ChargeBase):
    pass

class ChargeUpdate(BaseModel):
    studentId: int | None = None
    studentName: str | None = None
    dueDate: date | None = None
    amount: float | None = None
    status: str | None = None

class ChargeOut(ChargeBase):
    id: int

    class Config:
        from_attributes = True
