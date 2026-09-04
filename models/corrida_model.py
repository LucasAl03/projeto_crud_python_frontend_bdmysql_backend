from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, Date

from database import Base

class Corrida(Base):
    __tablename__ = "corrida"

    idcorrida = Column(Integer, primary_key=True, index=True)
    descricao_corrida = Column(String(200))
    data_corrida = Column(Date)
    distancia_5km = Column(String(5))
    distancia_10km = Column(String(5))
    distancia_25km = Column(String(5))
    
    
