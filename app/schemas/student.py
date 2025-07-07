from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional
import re

class StudentBase(BaseModel):
    profile_id: Optional[int] = Field(None, description="ID do perfil associado ao aluno")
    name: str = Field(..., description="Nome completo do aluno")
    ra: Optional[str] = Field(..., description="Registro acadêmico do aluno")
    cpf: Optional[str] = Field(..., description="CPF do aluno no formato 'xxx.xxx.xxx-xx'")
    email: EmailStr = Field(..., description="Email válido do aluno")
    gender: Optional[str] = Field(None, description="Sexo do aluno (ex: Masculino, Feminino, Outro)")
    birth_date: Optional[datetime] = Field(None, description="Data de nascimento do aluno (formato ISO 8601)")
    organization_id: Optional[int] = Field(..., description="ID da organização/polo a que o aluno pertence")
    organization_description: Optional[str] = Field(None, description="Descrição ou nome da organização/polo")

class StudentCreate(BaseModel):
    profile_id: Optional[int] = Field(None, description="ID do perfil associado ao aluno")
    name: str = Field(..., description="Nome completo do aluno")
    ra: Optional[str] = Field(..., description="Registro acadêmico do aluno")
    cpf: Optional[str] = Field(..., description="CPF do aluno no formato 'xxx.xxx.xxx-xx'")
    email: EmailStr = Field(..., description="Email válido do aluno")
    gender: Optional[str] = Field(None, description="Sexo do aluno (ex: Masculino, Feminino, Outro)")
    birth_date: Optional[datetime] = Field(None, description="Data de nascimento do aluno (formato ISO 8601)")
    organization_id: Optional[int] = Field(..., description="ID da organização/polo a que o aluno pertence")
    organization_description: Optional[str] = Field(None, description="Descrição ou nome da organização/polo")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Data e hora de criação do registro")

    @validator("cpf")
    def cpf_must_be_valid(cls, v: str) -> str:
        digits_only = re.sub(r"\D", "", v)

        if len(digits_only) != 11:
            raise ValueError("CPF deve conter 11 dígitos")

        return f"{digits_only[:3]}.{digits_only[3:6]}.{digits_only[6:9]}-{digits_only[9:]}"

    @validator("name")
    def name_must_have_min_length(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("Nome deve ter ao menos 3 caracteres")
        return v.title()

    @validator("gender")
    def gender_must_be_valid(cls, v):
        valid_genders = {"Masculino", "Feminino", "Outro", None}
        if v not in valid_genders:
            raise ValueError(f"Sexo deve ser um dos valores: {valid_genders}")
        return v

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Nome completo atualizado do aluno")
    email: Optional[EmailStr] = Field(None, description="Email atualizado do aluno")
    phone: Optional[str] = Field(None, description="Telefone atualizado do aluno")

class StudentOut(StudentBase):
    id: int = Field(..., description="ID único do aluno no sistema")

    class Config:
        from_attributes = True
        populate_by_name = True
