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
    
    id = Column(Integer, primary_key=True, index=True)  
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)  
    student_name = Column(String(100), nullable=False)  
    due_date = Column(Date, nullable=False)  
    amount = Column(Float, nullable=False)  
    amount_paid = Column(Float, nullable=False)  
    status = Column(Enum(ChargeStatus), nullable=False)  

    student = relationship("Student", back_populates="charges")
