from sqlalchemy import Column, DateTime, Integer, ForeignKey, Boolean, func
from sqlalchemy.orm import declared_attr

class AuditMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)

    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey("users.id"), nullable=True)

    @declared_attr
    def updated_by(cls):
        return Column(Integer, ForeignKey("users.id"), nullable=True)
