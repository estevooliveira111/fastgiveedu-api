from sqlalchemy import Column, Integer, String, Float, Date
from app.db.base import Base

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)