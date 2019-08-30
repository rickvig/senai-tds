from pessoa import Pessoa

class PessoaFisica(Pessoa):
    idade = 0
    sexo = ''
    cpf = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
       return 'nome: ' + self.nome + ', telefone: ' + self.telefone + ', idade: ' + str(self.idade)