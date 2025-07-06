from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    studentName: str
    amount: float
    date: datetime
    status: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    studentName: str | None = None
    amount: float | None = None
    date: datetime | None = None
    status: str | None = None

class PaymentOut(PaymentBase):
    id: int

    class Config:
        from_attributes = True
