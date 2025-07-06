from sqlalchemy import Column, Integer, String, Enum, Table
from app.db.base import Base
import enum

class AccountTypeEnum(str, enum.Enum):
    BANK_ACCOUNT = "BANK_ACCOUNT"
    CASH = "CASH"
    INVESTMENT = "INVESTMENT"

class StatusEnum(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class OperationEnum(str, enum.Enum):
    PAYMENT = "PAYMENT"
    TRANSFER = "TRANSFER"
    CASH_VIEW = "CASH_VIEW"
    RECEIPT = "RECEIPT"


polo_bank_account = Table(
    "polo_bank_account",
    Base.metadata,
    Column("polo_id", Integer, primary_key=True, comment="ID do polo"),
    Column("bank_account_id", Integer, primary_key=True, comment="ID da conta bancária"),
)

class BankAccount(Base):
    __tablename__ = "bank_accounts"
    __table_args__ = {"comment": "Tabela de contas bancárias vinculadas a polos"}

    id = Column(Integer, primary_key=True, index=True, comment="ID da conta bancária")
    name = Column(String(255), nullable=False, comment="Nome da conta bancária")
    number = Column(String(50), nullable=False, comment="Número da conta")
    dv_account = Column(String(10), nullable=True, comment="Dígito verificador da conta")
    account_type = Column(Enum(AccountTypeEnum), nullable=False, comment="Tipo da conta")
    sequential_file_remittance = Column(String(50), nullable=True, comment="Sequencial do arquivo de remessa")
    consolidated = Column(Integer, default=0, comment="Indica se a conta é consolidada (0 = não, 1 = sim)")
    bank_number = Column(String(20), nullable=True, comment="Número do banco")
    bank_name = Column(String(255), nullable=True, comment="Nome do banco")
    bank_code = Column(Integer, nullable=True, comment="Código do banco")
    agency_number = Column(String(50), nullable=True, comment="Número da agência")
    agency_dv = Column(String(10), nullable=True, comment="Dígito verificador da agência")
    agency_name = Column(String(255), nullable=True, comment="Nome da agência")
    agency_code = Column(Integer, nullable=True, comment="Código da agência")
    status = Column(Enum(StatusEnum), nullable=False, comment="Status da conta (ATIVO/INATIVO)")
    operation = Column(Enum(OperationEnum), nullable=True, comment="Tipo de operação permitida para a conta")
