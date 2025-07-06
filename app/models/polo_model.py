from sqlalchemy import Column, Integer, String, DateTime
from app.models.base_mixin import AuditMixin
from app.db.base import Base

class Polo(Base, AuditMixin):
    __tablename__ = "polos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment="Identificador único da tabela (chave primária)")
    physical_unit_id = Column(Integer, index=True, nullable=True, comment="ID obrigatório da unidade física, único")
    name = Column(String(255), nullable=False, comment="Nome do polo (obrigatório)")
    print_name = Column(String(255), nullable=True, comment="Nome para impressão")
    acronym = Column(String(50), nullable=True, comment="Sigla do polo")
    street = Column(String(255), nullable=True, comment="Logradouro (endereço)")
    number = Column(String(20), nullable=True, comment="Número do endereço")
    neighborhood = Column(String(100), nullable=True, comment="Bairro")
    postal_code = Column(String(20), nullable=True, comment="CEP")
    email = Column(String(100), nullable=True, comment="E-mail")
    cnpj = Column(String(20), nullable=True, comment="CNPJ da unidade")
    phones = Column(String(100), nullable=True, comment="Telefones de contato")
    city_id = Column(Integer, nullable=True, comment="ID da cidade")
    state_id = Column(Integer, nullable=True, comment="ID do estado")
    status = Column(String(50), nullable=True, comment="Status do polo (ativo, inativo, etc)")
    activation_date = Column(DateTime, nullable=True, comment="Data de ativação da unidade")
    inactivation_date = Column(DateTime, nullable=True, comment="Data de inativação da unidade")
    inep_code = Column(Integer, nullable=True, comment="Código INEP")
    city_name = Column(String(100), nullable=True, comment="Nome da cidade")
    state_acronym = Column(String(10), nullable=True, comment="Sigla do estado")
    state_name = Column(String(100), nullable=True, comment="Nome do estado")
    responsible_name = Column(String(255), nullable=True, comment="Nome do responsável")
    responsible_phone = Column(String(50), nullable=True, comment="Telefone do responsável")
    responsible_cellphone = Column(String(50), nullable=True, comment="Celular do responsável")
    responsible_email = Column(String(100), nullable=True, comment="E-mail do responsável")
    responsible_profile_id = Column(Integer, nullable=True, comment="ID do perfil do responsável")
    supervisor_name = Column(String(255), nullable=True, comment="Nome do supervisor")
    supervisor_profile_id = Column(Integer, nullable=True, comment="ID do perfil do supervisor")
    hide_in_form = Column(Integer, nullable=True, comment="Indica se não apresenta no formulário de atendimento (0 ou 1)")
    complement = Column(String(255), nullable=True, comment="Complemento do endereço")
    unit_type = Column(String(100), nullable=True, comment="Tipo da unidade")
    attendance_hours_note = Column(String(255), nullable=True, comment="Observação sobre horário de atendimento")