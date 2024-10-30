from app import db
from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import relationship, aliased
from datetime import datetime
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Tabela de Pacientes
class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date)
    telefone = db.Column(db.String(15))
    endereco = db.Column(db.String(255))
    historico_medico = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    consultas = db.relationship("Consulta", back_populates="paciente", cascade="all, delete")
    exames = db.relationship("Exame", back_populates="paciente", cascade="all, delete")


# Tabela de Médicos
class Medico(db.Model):
    __tablename__ = 'medicos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    especializacao = db.Column(db.String(100))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    consultas = db.relationship("Consulta", back_populates="medico", cascade="all, delete")


# Tabela de Consultas
class Consulta(db.Model):
    __tablename__ = 'consultas'
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id', ondelete="CASCADE"))
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id', ondelete="SET NULL"))
    data_consulta = db.Column(db.DateTime, nullable=False)
    motivo_consulta = db.Column(db.String(255))
    diagnostico = db.Column(db.Text)
    prescricao = db.Column(db.Text)
    follow_up = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    paciente = db.relationship("Paciente", back_populates="consultas")
    medico = db.relationship("Medico", back_populates="consultas")
    prescricoes = db.relationship("Prescricao", back_populates="consulta", cascade="all, delete")
    notificacoes = db.relationship("Notificacao", back_populates="consulta", cascade="all, delete")


# Tabela de Prescrições
class Prescricao(db.Model):
    __tablename__ = 'prescricoes'
    
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id', ondelete="CASCADE"))
    medicamento = db.Column(db.String(100), nullable=False)
    dosagem = db.Column(db.String(50))
    frequencia = db.Column(db.String(50))
    duracao = db.Column(db.String(50))
    observacoes = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    consulta = db.relationship("Consulta", back_populates="prescricoes")


# Tabela de Exames
class Exame(db.Model):
    __tablename__ = 'exames'
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id', ondelete="CASCADE"))
    tipo_exame = db.Column(db.String(100), nullable=False)
    data_exame = db.Column(db.Date, nullable=False)
    resultado = db.Column(db.Text)
    observacoes = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    paciente = db.relationship("Paciente", back_populates="exames")


# Tabela de Usuários
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    nome_completo = db.Column(db.String(100))
    perfil = db.Column(db.String(100))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)


# Tabela de Notificações
class Notificacao(db.Model):
    __tablename__ = 'notificacoes'
    
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id', ondelete="CASCADE"))
    mensagem = db.Column(db.String(255))
    data_envio = db.Column(db.DateTime, default=datetime.now)
    enviada = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    consulta = db.relationship("Consulta", back_populates="notificacoes")