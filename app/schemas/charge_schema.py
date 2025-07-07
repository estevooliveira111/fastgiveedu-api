from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Literal

class ChargeBase(BaseModel):
    student_id: int = Field(..., description="Identificador único do aluno")
    due_date: date = Field(..., description="Data de vencimento da cobrança")
    amount: float = Field(..., description="Valor total da cobrança")
    status: str = Field(..., description="Status da cobrança (ex: PENDING, PAID, OVERDUE)")

class ChargeCreate(BaseModel):
    student_id: int = Field(..., description="Identificador único do aluno")
    due_date: date = Field(..., description="Data de vencimento da cobrança")
    amount: float = Field(..., gt=0, description="Valor total da cobrança. Deve ser maior que zero")
    status: Literal["PENDING", "PAID", "OVERDUE"] = Field(..., description="Status da cobrança")

    @validator("due_date")
    def due_date_not_in_past(cls, v):
        if v < date.today():
            raise ValueError("A data de vencimento não pode ser no passado")
        return v

class ChargeUpdate(BaseModel):
    student_id: int | None = Field(None, description="Identificador do aluno para atualização (opcional)")
    due_date: date | None = Field(None, description="Data de vencimento para atualização (opcional)")
    amount: float | None = Field(None, description="Valor da cobrança para atualização (opcional)")
    status: str | None = Field(None, description="Status da cobrança para atualização (opcional)")

class ChargeOut(ChargeBase):
    id: int = Field(..., description="Identificador único da cobrança")

    class Config:
        from_attributes = True