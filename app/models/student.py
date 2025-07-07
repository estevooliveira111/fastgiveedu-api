from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    organization_id = Column(Integer, nullable=True)
