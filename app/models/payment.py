from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False)
