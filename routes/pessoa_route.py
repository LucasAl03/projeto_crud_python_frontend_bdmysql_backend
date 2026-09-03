from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal

from controllers.pessoa_controller import PessoaController
from schemas.pessoa_schema import PessoaSchema

router = APIRouter(
    prefix="/pessoa",
    tags=["Pessoa"]
)
controller = PessoaController()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar():
    db = next(get_db())

    return controller.listar(db)

@router.get("/{idpessoa}")
def listar_id(idpessoa: int):
    db = next(get_db())

    return controller.listar_id(db, idpessoa)

@router.post("/")
def cadstrar(pessoa: PessoaSchema):
    db = next(get_db())
    return controller.cadastrar(db, pessoa)

@router.put("/{idpessoa}")
def alterar(idpessoa: int, pessoa: PessoaSchema):

    db = next(get_db())

    return controller.alterar(
        db,
        idpessoa,
        pessoa
    )

@router.delete("/{idpessoa}")
def excluir(idpessoa: int):

    db = next(get_db())

    return controller.excluir(
        db,
        idpessoa
    )