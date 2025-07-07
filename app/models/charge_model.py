from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.models.base_mixin import AuditMixin
from app.db.base import Base
import enum

class ChargeStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

class Charge(Base, AuditMixin):
    __tablename__ = "charges"
    
    id = Column(Integer, primary_key=True, index=True, comment="Identificador único da cobrança")

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False, comment="Chave estrangeira que referencia o aluno")
    due_date = Column(Date, nullable=False, comment="Data de vencimento da cobrança")

    payment_date = Column(Date, nullable=True, comment="Data em que o pagamento foi realizado (pode ser nula se ainda não pago)")
    amount = Column(Float, nullable=True, comment="Valor total da cobrança")
    amount_paid = Column(Float, nullable=True, comment="Valor efetivamente pago (pode ser menor, igual ou maior que o valor original)")
    status = Column(Enum(ChargeStatus), nullable=False, comment="Status atual da cobrança: PENDING (pendente), PAID (paga), OVERDUE (vencida)")
    student = relationship("Student", back_populates="charges")