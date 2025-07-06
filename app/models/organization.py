from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    document = Column(String(18), unique=True, nullable=True)
