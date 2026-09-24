# Importar bibliotecas
from sqlalchemy import create_engine, func, Column, Integer, String, DateTime, ForeignKey, Date, Text
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

#Base de dados - endereço
engine = create_engine('mysql+pymysql://root:root@localhost:3306/taskflow')

#Config sessao
db_session = sessionmaker(bind=engine)

Base = declarative_base()

class Recurso_tarefa(Base):
    __tablename__ = 'recurso_tarefas'
    id = Column(Integer, primary_key=True)
    tarefa_id = Column(Integer, ForeignKey('tarefas.id'), nullable=False)
    recurso_id = Column(Integer, ForeignKey('recursos.id'), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    papel = Column(String(100), default='usuario', nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

class Recurso(Base):
    __tablename__ = 'recursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    desc = Column(Text, nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

class Tarefa(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    data = Column(Date, nullable=False, server_default=func.now())
    categoria = Column(String(100), nullable=False, server_default=func.now())
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    tipo_id = Column(Integer, ForeignKey('tipos.id'), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())

class Tipo(Base):
    __tablename__ = 'tipos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())


    def __repr__(self):
        return f'Pessoa {self.nome}, email: {self.email}>'
