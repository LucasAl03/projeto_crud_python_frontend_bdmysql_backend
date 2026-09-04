from pydantic import BaseModel
from datetime import date

class CorridaSchema(BaseModel):
    descricao_corrida : str
    data_corrida: date
    distancia_5km: str
    distancia_10km: str
    distancia_25km: str


    