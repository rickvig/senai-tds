from pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, nome, idade, sexo):
        self.sexo = sexo

    def __str__(self):
       return 'nome: ' + self.nome + ', telefone: ' + self.telefone + ', idade: ' + str(self.idade)