from pydantic import BaseModel
from datetime import date

class PessoaSchema(BaseModel):
    nome : str
    cpf: str
    data_nascimento: date
    peso: float
    altura: float
    sexo : str
    idade : int
    imc : float
    cep : str
    rua_logradouro : str
    bairro : str
    cidade : str
    uf : str
    