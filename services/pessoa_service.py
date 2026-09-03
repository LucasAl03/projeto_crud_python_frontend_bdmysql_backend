from repositories.pessoa_repository import PessoaRepository

class PessoaService:
    #método contrutor
    def __init__(self):
        self.repo = PessoaRepository()

    #serviço listar
    def listar(self, db):
        return self.repo.listar(db)

    #serviço listar_id
    def listar_id(self, db, idpessoa):
        return self.repo.pessoa_id(db, idpessoa)
    
    #serviço cadastrar
    def cadastar(self, db, pessoa):
        return self.repo.cadastar(db, pessoa)

    # serviço alterar
    def alterar(self, db, idpessoa, pessoa):
        return self.repo.alterar(db, idpessoa, pessoa)


    # serviço excluir
    def excluir(self, db, idpessoa):
        return self.repo.excluir(db, idpessoa)
