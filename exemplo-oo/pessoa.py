class Pessoa(object):
    nome = ''
    telefone = ''
    
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
       return 'nome: ' + self.nome + ', telefone: ' + self.telefone