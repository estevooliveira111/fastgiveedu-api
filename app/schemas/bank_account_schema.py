from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class AccountTypeEnum(str, Enum):
    BANK_ACCOUNT = "BANK_ACCOUNT"
    CASH = "CASH"
    INVESTMENT = "INVESTMENT"

class StatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class OperationEnum(str, Enum):
    PAYMENT = "PAYMENT"
    TRANSFER = "TRANSFER"
    CASH_VIEW = "CASH_VIEW"
    RECEIPT = "RECEIPT"

class BankAccountBase(BaseModel):
    name: str = Field(..., description="Nome da conta bancária")
    number: str = Field(..., description="Número da conta")
    dv_account: Optional[str] = Field(None, description="Dígito verificador da conta")
    account_type: AccountTypeEnum = Field(..., description="Tipo da conta")
    sequential_file_remittance: Optional[str] = Field(None, description="Sequencial do arquivo de remessa")
    consolidated: Optional[int] = Field(0, description="Conta consolidada (0 ou 1)")
    bank_number: Optional[str] = Field(None, description="Número do banco")
    bank_name: Optional[str] = Field(None, description="Nome do banco")
    bank_code: Optional[int] = Field(None, description="Código do banco")
    agency_number: Optional[str] = Field(None, description="Número da agência")
    agency_dv: Optional[str] = Field(None, description="Dígito verificador da agência")
    agency_name: Optional[str] = Field(None, description="Nome da agência")
    agency_code: Optional[int] = Field(None, description="Código da agência")
    status: StatusEnum = Field(..., description="Status da conta (ATIVO/INATIVO)")
    operation: Optional[OperationEnum] = Field(None, description="Operação permitida")

class BankAccountCreate(BaseModel):
    name: str = Field(..., description="Nome da conta bancária")
    number: str = Field(..., description="Número da conta")
    dv_account: Optional[str] = Field(None, description="Dígito verificador da conta")
    account_type: AccountTypeEnum = Field(..., description="Tipo da conta")
    sequential_file_remittance: Optional[str] = Field(None, description="Sequencial do arquivo de remessa")
    consolidated: Optional[int] = Field(0, description="Conta consolidada (0 ou 1)")
    bank_number: Optional[str] = Field(None, description="Número do banco")
    bank_name: Optional[str] = Field(None, description="Nome do banco")
    bank_code: Optional[int] = Field(None, description="Código do banco")
    agency_number: Optional[str] = Field(None, description="Número da agência")
    agency_dv: Optional[str] = Field(None, description="Dígito verificador da agência")
    agency_name: Optional[str] = Field(None, description="Nome da agência")
    agency_code: Optional[int] = Field(None, description="Código da agência")
    status: StatusEnum = Field(..., description="Status da conta (ATIVO/INATIVO)")
    operation: Optional[OperationEnum] = Field(None, description="Operação permitida")

    polo_id: Optional[int] = Field(None, description="ID do polo para associação direta")

class BankAccountUpdate(BankAccountBase):
    pass

class BankAccountOut(BankAccountBase):
    id: int = Field(..., description="ID da conta bancária")

    class Config:
        from_attributes = True

class PaginatedBankAccountOut(BaseModel):
    data: List[BankAccountOut]
    page: int
    page_size: int
    total_pages: int
    total_items: int
