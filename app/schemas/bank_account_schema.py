from pydantic import BaseModel
from typing import Optional

class BankAccountBase(BaseModel):
    bank_name: str
    account_number: str
    agency: str
    campus_id: int

class BankAccountCreate(BankAccountBase):
    pass

class BankAccountUpdate(BaseModel):
    bank_name: Optional[str]
    account_number: Optional[str]
    agency: Optional[str]

class BankAccountOut(BankAccountBase):
    id: int

    class Config:
        from_attributes = True