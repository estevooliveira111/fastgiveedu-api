from sqlalchemy import Column, Integer, Float, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.db.base import Base

class AmountType(PyEnum):
    ABSOLUTE = "ABSOLUTE"
    PERCENTAGE = "PERCENTAGE"

class ChargeSplit(Base):
    __tablename__ = "charge_splits"

    id = Column(Integer, primary_key=True, index=True)

    charge_id = Column(Integer, ForeignKey("charges.id"), nullable=False, comment="ID da cobrança relacionada")
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False, comment="ID da conta bancária para rateio")

    polo_id = Column(Integer, ForeignKey("polos.id"), nullable=False, comment="ID do polo associado ao rateio")

    account_name = Column(String(100), nullable=False, comment="Nome da conta/centro de custo para o rateio")
    amount = Column(Float, nullable=False, comment="Valor do rateio (absoluto ou percentual)")
    amount_type = Column(Enum(AmountType), nullable=False, comment="Tipo do valor: ABSOLUTO ou PERCENTUAL")

    charge = relationship("Charge", back_populates="splits")
    bank_account = relationship("BankAccount")
    polo = relationship("Polo")
