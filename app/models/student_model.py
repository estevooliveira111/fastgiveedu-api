from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base
from app.models.base_mixin import AuditMixin


class Student(Base, AuditMixin):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, comment="ID único do aluno")

    profile_id = Column(
        Integer, nullable=True, comment="ID do perfil associado ao aluno"
    )

    name = Column(String(100), nullable=False, comment="Nome completo do aluno")

    ra = Column(String(50), nullable=True, comment="RA (registro acadêmico) do aluno")

    cpf = Column(
        String(14), nullable=True, unique=True, comment="CPF do aluno (deve ser único)"
    )

    email = Column(
        String(100),
        nullable=True,
        unique=True,
        comment="E-mail do aluno (deve ser único)",
    )

    gender = Column(
        String(20),
        nullable=True,
        comment="Sexo do aluno (ex: Masculino, Feminino, Outro)",
    )

    birth_date = Column(DateTime, nullable=True, comment="Data de nascimento do aluno")

    organization_id = Column(
        Integer, nullable=True, comment="ID da organização ou polo vinculada ao aluno"
    )

    organization_description = Column(
        String(100), nullable=True, comment="Descrição da organização ou polo do aluno"
    )

    created_at = Column(
        DateTime, default=datetime.utcnow, comment="Data de criação do registro"
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        comment="Data da última modificação do registro",
    )

    charges = relationship(
        "Charge", back_populates="student"
    )
