from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Charge(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=False)
    student_name = Column(String(100), nullable=False)
    due_date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)