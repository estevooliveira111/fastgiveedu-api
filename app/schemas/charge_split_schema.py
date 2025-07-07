from pydantic import BaseModel, Field, validator
from enum import Enum
from typing import Optional

class AmountTypeEnum(str, Enum):
    ABSOLUTE = "ABSOLUTE"
    PERCENTAGE = "PERCENTAGE"

class ChargeSplitBase(BaseModel):
    charge_id: Optional[int] = Field(None, description="ID da cobrança relacionada")
    bank_account_id: Optional[int] = Field(None, description="ID da conta bancária para rateio")
    polo_id: Optional[int] = Field(None, description="ID do polo associado ao rateio")
    account_name: Optional[str] = Field(None, max_length=100, description="Nome da conta/centro de custo para o rateio")
    amount: Optional[float] = Field(None, description="Valor do rateio (absoluto ou percentual)")
    amount_type: Optional[AmountTypeEnum] = Field(None, description="Tipo do valor: ABSOLUTO ou PERCENTUAL")

    @validator("amount")
    def validate_amount(cls, v, values):
        if "amount_type" in values and values["amount_type"] == AmountTypeEnum.PERCENTAGE:
            if not (0 < v <= 100):
                raise ValueError("Para valor percentual, o valor deve ser maior que 0 e menor ou igual a 100")
        return v

class ChargeSplitCreate(ChargeSplitBase):
    bank_account_id: int
    polo_id: int
    account_name: str
    amount: float
    amount_type: AmountTypeEnum

class ChargeSplitUpdate(BaseModel):
    bank_account_id: Optional[int] = Field(None, description="ID da conta bancária para rateio")
    account_name: Optional[str] = Field(None, max_length=100, description="Nome da conta/centro de custo para o rateio")
    amount: Optional[float] = Field(None, gt=0, description="Valor do rateio (absoluto ou percentual)")
    amount_type: Optional[AmountTypeEnum] = Field(None, description="Tipo do valor: ABSOLUTE ou PERCENTAGE")

    @validator("amount")
    def validate_amount(cls, v, values):
        if "amount_type" in values and values["amount_type"] == AmountTypeEnum.PERCENTAGE:
            if not (0 < v <= 100):
                raise ValueError("Para valor percentual, o valor deve ser maior que 0 e menor ou igual a 100")
        return v

class ChargeSplitOut(ChargeSplitBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
