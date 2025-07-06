from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Polo(Base):
    __tablename__ = "polos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)