from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import datetime

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    email = Column(String)
    data_registro = Column(DateTime, default=datetime.datetime.now)
    
    veiculos = relationship("Veiculo", back_populates="cliente")
    agendamentos = relationship("Agendamento", back_populates="cliente")

class Veiculo(Base):
    __tablename__ = 'veiculo'
    id_veiculo = Column(Integer, primary_key=True)
    placa = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    cor = Column(String)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'))
    
    cliente = relationship("Cliente", back_populates="veiculos")
    agendamentos = relationship("Agendamento", back_populates="veiculo")

class Servico(Base):
    __tablename__ = 'servico'
    id_servico = Column(Integer, primary_key=True)
    descricao = Column(String)
    preco = Column(Float)
    duracao = Column(Float)
    
    agendamentos = relationship("Agendamento", back_populates="servico")

class Agendamento(Base):
    __tablename__ = 'agendamento'
    id_agendamento = Column(Integer, primary_key=True)
    data = Column(DateTime)
    hora = Column(DateTime)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'))
    id_veiculo = Column(Integer, ForeignKey('veiculo.id_veiculo'))
    id_servico = Column(Integer, ForeignKey('servico.id_servico'))
    
    cliente = relationship("Cliente", back_populates="agendamentos")
    veiculo = relationship("Veiculo", back_populates="agendamentos")
    servico = relationship("Servico", back_populates="agendamentos")
    atendimentos = relationship("Atendimento", back_populates="agendamento")

class Funcionario(Base):
    __tablename__ = 'funcionario'
    id_funcionario = Column(Integer, primary_key=True)
    nome = Column(String)
    cargo = Column(String)
    telefone = Column(String)
    email = Column(String)
    
    atendimentos = relationship("Atendimento", back_populates="funcionario")

class Oficina(Base):
    __tablename__ = 'oficina'
    id_oficina = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    
    atendimentos = relationship("Atendimento", back_populates="oficina")

class Atendimento(Base):
    __tablename__ = 'atendimento'
    id_atendimento = Column(Integer, primary_key=True)
    data = Column(DateTime)
    hora = Column(DateTime)
    id_funcionario = Column(Integer, ForeignKey('funcionario.id_funcionario'))
    id_oficina = Column(Integer, ForeignKey('oficina.id_oficina'))
    id_agendamento = Column(Integer, ForeignKey('agendamento.id_agendamento'))
    
    funcionario = relationship("Funcionario", back_populates="atendimentos")
    oficina = relationship("Oficina", back_populates="atendimentos")
    agendamento = relationship("Agendamento", back_populates="atendimentos")

engine = create_engine('sqlite:///oficina.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

novo_cliente = Cliente(nome="Gian Souza", endereco="Rua 7, Casa 345", telefone="9212345678", email="gian_souza123@gmail.com")
session.add(novo_cliente)
session.commit()

print("Cliente adicionado com sucesso!")
