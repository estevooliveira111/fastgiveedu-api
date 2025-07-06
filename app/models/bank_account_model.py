from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String(100), nullable=False, comment="Account holder or name")
    bank_name = Column(String(50), nullable=False, comment="Bank name")
    agency_number = Column(String(20), nullable=False, comment="Bank agency number")
    account_number = Column(String(20), nullable=False, comment="Bank account number")

    campus_id = Column(Integer, nullable=False, comment="Foreign key to Campus")
    campus = relationship("Campus", back_populates="bank_accounts")