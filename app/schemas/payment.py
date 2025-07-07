from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Literal

class PaymentBase(BaseModel):
    amount: float = Field(..., description="Valor pago pelo aluno")
    date: datetime = Field(..., description="Data em que o pagamento foi realizado")
    status: str = Field(..., description="Status do pagamento, ex: 'PENDING', 'PAID', 'FAILED'")

class PaymentCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Valor pago pelo aluno. Deve ser maior que zero")
    date: datetime = Field(..., description="Data em que o pagamento foi realizado")
    status: Literal["PENDING", "PAID", "FAILED"] = Field(..., description="Status do pagamento")

class PaymentUpdate(BaseModel):
    amount: float | None = Field(None, description="Valor pago para atualização")
    date: datetime | None = Field(None, description="Data do pagamento para atualização")
    status: str | None = Field(None, description="Status do pagamento para atualização")

class PaymentOut(PaymentBase):
    id: int = Field(..., description="Identificador único do pagamento")

    class Config:
        from_attributes = True
        populate_by_name = True