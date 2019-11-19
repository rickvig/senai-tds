class Pessoa(object):
    
    def __init__(self, nome, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __str__(self):
       return 'nome: ' + self.nome + ', idade: ' + self.idade + ', telefone: ' + self.telefone