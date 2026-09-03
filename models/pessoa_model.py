from sqlalchemy import Column, Integer, String, DECIMAL

from database import Base

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    idpessoa = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60))
    cpf = Column(String(11))
    dataNascimento = Column(String)
    peso = Column(DECIMAL(10,2))
    altura = Column(DECIMAL(10,2))
    sexo = Column(String(1))
    cep = Column(String(9))
    ruaLogradouro = Column(String(100))
    bairro = Column(String(20))
    cidade = Column(String(70))
    uf = Column(String(2))
    
    
   

