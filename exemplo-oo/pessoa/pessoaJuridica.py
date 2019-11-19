from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nomefantasia, cnpj):
        self.nomefantasia = nomefantasia
        self.cnpj = cnpj
    
    def __str__(self):
        return "Pessoa: {0} \n Juridica: {1}, CNPJ: {2}".format(
            super().__str__(), 
            self.nomefantasia, 
            self.cnpj)