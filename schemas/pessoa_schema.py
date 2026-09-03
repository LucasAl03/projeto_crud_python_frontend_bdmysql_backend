from pydantic import BaseModel
from datetime import date

class PessoaSchema(BaseModel):
    nome : str
    cpf: str
    dataNascimento: str
    peso: float
    altura: float
    sexo : str
    cep : str
    ruaLogradouro : str
    bairro : str
    cidade : str
    uf : str
    