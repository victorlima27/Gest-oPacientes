from app import db
from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import relationship, aliased
from datetime import datetime


# Modelo para Pacientes
class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date)
    telefone = db.Column(db.String(15))
    historico_medico = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relacionamento com consultas
    consultas = db.relationship('Consulta', backref='paciente', cascade="all, delete-orphan")

    # Relacionamento com exames
    exames = db.relationship('Exame', backref='paciente', cascade="all, delete-orphan")


# Modelo para Médicos
class Medico(db.Model):
    __tablename__ = 'medicos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    especializacao = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relacionamento com consultas
    consultas = db.relationship('Consulta', backref='medico', cascade="all, delete-orphan")

    # Relacionamento com exames
    exames = db.relationship('Exame', backref='medico', cascade="all, delete-orphan")


# Modelo para Consultas
class Consulta(db.Model):
    __tablename__ = 'consultas'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id', ondelete='CASCADE'))
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id', ondelete='SET NULL'))
    data_consulta = db.Column(db.DateTime, nullable=False)
    motivo_consulta = db.Column(db.String(255))
    diagnostico = db.Column(db.Text)
    prescricao = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relacionamento com notificações
    notificacoes = db.relationship('Notificacao', backref='consulta', cascade="all, delete-orphan")


# Modelo para Exames
class Exame(db.Model):
    __tablename__ = 'exames'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id', ondelete='CASCADE'))
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id', ondelete='CASCADE'))
    tipo_exame = db.Column(db.String(100), nullable=False)
    data_exame = db.Column(db.Date, nullable=False)
    resultado = db.Column(db.Text)
    observacoes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


# Modelo para Usuários
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    nome_completo = db.Column(db.String(100))
    perfil = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


# Modelo para Notificações
class Notificacao(db.Model):
    __tablename__ = 'notificacoes'
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id', ondelete='CASCADE'))
    mensagem = db.Column(db.String(255))
    data_envio = db.Column(db.DateTime, default=db.func.current_timestamp())
    enviada = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())