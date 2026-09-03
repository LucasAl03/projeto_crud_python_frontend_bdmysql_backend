from services.pessoa_service import PessoaService

class PessoaController:
    #método construtor
    def __init__(self):
        self.servico = PessoaService()
    
    #controler listar
    def listar(self, db):
        return self.servico.listar(db)

    #controler listar_id
    def listar_id(self, db, idpessoa):
        return self.servico.listar_id(db, idpessoa)
    
    #controle cadastrar
    def cadastar(self, db, pessoa):
        return self.servico.cadastar(db, pessoa)

  # controller alterar pessoa
    def alterar(self, db, idpessoa, pessoa):
        return self.servico.alterar(db, idpessoa, pessoa)


    # controller excluir pessoa
    def excluir(self, db, idpessoa):
        return self.servico.excluir(db, idpessoa)