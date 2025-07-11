from sqlalchemy import Column, Integer, String
from app.models.base_mixin import AuditMixin
from app.db.base import Base

class User(Base, AuditMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    organization_id = Column(Integer, nullable=True)