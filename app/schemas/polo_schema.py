from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class PoloBase(BaseModel):
    physical_unit_id: Optional[int] = Field(None, description="ID da Unidade Física (obrigatório)")
    name: Optional[str] = Field(None, description="Nome do polo")
    print_name: Optional[str] = Field(None, description="Nome para impressão")
    acronym: Optional[str] = Field(None, description="Sigla do polo")
    street: Optional[str] = Field(None, description="Logradouro")
    number: Optional[str] = Field(None, description="Número")
    neighborhood: Optional[str] = Field(None, description="Bairro")
    postal_code: Optional[str] = Field(None, description="CEP")
    email: Optional[EmailStr] = Field(None, description="Email")
    cnpj: Optional[str] = Field(None, description="CNPJ")
    phones: Optional[str] = Field(None, description="Telefones")
    city_id: Optional[int] = Field(None, description="ID da cidade")
    state_id: Optional[int] = Field(None, description="ID do estado")
    status: Optional[str] = Field(None, description="Status")
    activation_date: Optional[datetime] = Field(None, description="Data de ativação")
    inactivation_date: Optional[datetime] = Field(None, description="Data de inativação")
    inep_code: Optional[int] = Field(None, description="Código INEP")
    city_name: Optional[str] = Field(None, description="Nome da cidade")
    state_acronym: Optional[str] = Field(None, description="Sigla do estado")
    state_name: Optional[str] = Field(None, description="Nome do estado")
    responsible_name: Optional[str] = Field(None, description="Nome do responsável")
    responsible_phone: Optional[str] = Field(None, description="Telefone do responsável")
    responsible_cellphone: Optional[str] = Field(None, description="Celular do responsável")
    responsible_email: Optional[EmailStr] = Field(None, description="Email do responsável")
    responsible_profile_id: Optional[int] = Field(None, description="ID do perfil do responsável")
    supervisor_name: Optional[str] = Field(None, description="Nome do supervisor")
    supervisor_profile_id: Optional[int] = Field(None, description="ID do perfil do supervisor")
    hide_in_form: Optional[int] = Field(None, description="Não apresentar no formulário de atendimento (0 ou 1)")
    complement: Optional[str] = Field(None, description="Complemento")
    unit_type: Optional[str] = Field(None, description="Tipo da unidade")
    attendance_hours_note: Optional[str] = Field(None, description="Observação sobre horário de atendimento")

class PoloCreate(PoloBase):
    pass

class PoloUpdate(BaseModel):
    physical_unit_id: Optional[int] = Field(None, description="ID da Unidade Física (obrigatório)")
    name: Optional[str] = Field(None, description="Nome do polo")
    print_name: Optional[str] = Field(None, description="Nome para impressão")
    acronym: Optional[str] = Field(None, description="Sigla do polo")
    street: Optional[str] = Field(None, description="Logradouro")
    number: Optional[str] = Field(None, description="Número")
    neighborhood: Optional[str] = Field(None, description="Bairro")
    postal_code: Optional[str] = Field(None, description="CEP")
    email: Optional[EmailStr] = Field(None, description="Email")
    cnpj: Optional[str] = Field(None, description="CNPJ")
    phones: Optional[str] = Field(None, description="Telefones")
    city_id: Optional[int] = Field(None, description="ID da cidade")
    state_id: Optional[int] = Field(None, description="ID do estado")
    status: Optional[str] = Field(None, description="Status")
    activation_date: Optional[datetime] = Field(None, description="Data de ativação")
    inactivation_date: Optional[datetime] = Field(None, description="Data de inativação")
    inep_code: Optional[int] = Field(None, description="Código INEP")
    city_name: Optional[str] = Field(None, description="Nome da cidade")
    state_acronym: Optional[str] = Field(None, description="Sigla do estado")
    state_name: Optional[str] = Field(None, description="Nome do estado")
    responsible_name: Optional[str] = Field(None, description="Nome do responsável")
    responsible_phone: Optional[str] = Field(None, description="Telefone do responsável")
    responsible_cellphone: Optional[str] = Field(None, description="Celular do responsável")
    responsible_email: Optional[EmailStr] = Field(None, description="Email do responsável")
    responsible_profile_id: Optional[int] = Field(None, description="ID do perfil do responsável")
    supervisor_name: Optional[str] = Field(None, description="Nome do supervisor")
    supervisor_profile_id: Optional[int] = Field(None, description="ID do perfil do supervisor")
    hide_in_form: Optional[int] = Field(None, description="Não apresentar no formulário de atendimento (0 ou 1)")
    complement: Optional[str] = Field(None, description="Complemento")
    unit_type: Optional[str] = Field(None, description="Tipo da unidade")
    attendance_hours_note: Optional[str] = Field(None, description="Observação sobre horário de atendimento")

class PoloOut(PoloBase):
    id: int = Field(..., description="ID do registro")

    class Config:
        from_attributes = True
        populate_by_name = True


class PaginatedPoloOut(BaseModel):
    data: List[PoloOut] = []  
    page: int = 1            
    page_size: int = 10      
    total_pages: int = 1     
    total_items: int = 0     

    class Config:
        schema_extra = {
            "example": {
                "data": [],
                "page": 1,
                "page_size": 10,
                "total_pages": 5,
                "total_items": 45,
            }
        }

