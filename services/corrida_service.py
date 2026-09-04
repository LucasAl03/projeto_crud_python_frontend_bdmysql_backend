from repositories.corrida_repository import CorridaRepository

class CorridaService:
    #método contrutor
    def __init__(self):
        self.repo = CorridaRepository()

    #serviço listar
    def listar(self, db):
        return self.repo.listar(db)

    #serviço listar_id
    def listar_id(self, db, idcorrida):
        return self.repo.corrida_id(db, idcorrida)
    
    #serviço cadastrar
    def cadastrar(self, db, corrida):
        return self.repo.cadastrar(db, corrida)

    # serviço alterar
    def alterar(self, db, idcorrida, corrida):
        return self.repo.alterar(db, idcorrida, corrida)

    # serviço excluir
    def excluir(self, db, idcorrida):
        return self.repo.excluir(db, idcorrida)
