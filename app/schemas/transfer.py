from pydantic import BaseModel
from datetime import date

class TransferBase(BaseModel):
    recipient: str
    amount: float
    date: date
    status: str

class TransferCreate(TransferBase):
    pass

class TransferUpdate(BaseModel):
    recipient: str | None = None
    amount: float | None = None
    date: str | None = None
    status: str | None = None

class TransferOut(TransferBase):
    id: int

    class Config:
        from_attributes = True
