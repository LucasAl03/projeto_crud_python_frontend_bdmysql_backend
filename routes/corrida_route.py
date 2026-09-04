from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal

from controllers.pessoa_controller import PessoaController
from schemas.pessoa_schema import PessoaSchema
from controllers.corrida_controller import CorridaController
from schemas.corrida_schema import CorridaSchema

router = APIRouter(
    prefix="/corrida",
    tags=["Corrida"]
)

controller = CorridaController()

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

@router.get("/{idcorrida}")
def listar_id(idcorrida: int):
    db = next(get_db())

    return controller.listar_id(db, idcorrida)

@router.post("/")
def cadastrar(corrida: CorridaSchema):
    db = next(get_db())
    return controller.cadastrar(db, corrida)

@router.put("/{idcorrida}")
def alterar(idcorrida: int, corrida: CorridaSchema):

    db = next(get_db())

    return controller.alterar(
        db,
        idcorrida,
        corrida
    )

@router.delete("/{idcorrida}")
def excluir(idcorrida: int):

    db = next(get_db())

    return controller.excluir(
        db,
        idcorrida
    )