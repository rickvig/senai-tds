class Pessoa(object):
    nome = ''
    telefone = ''
    
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
       return 'nome: ' + self.nome + ', telefone: ' + self.telefone 


pessoa = Pessoa("Henrique", "(44) 99941-0923")
print(pessoa)



class PessoaFisica(Pessoa):
    idade = 0
    sexo = ''
    cpf = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

lorena = PessoaFisica("Lorena", 27)
print(lorena)
print(lorena.telefone)
print(lorena.idade, lorena.cpf)
print(lorena.cpf)

# class PessoaJuridica(Pessoa):
#     nomefantasia = ''
#     cnpj = 0

#     def __init__(self, nomefantasia):
#         self.nomefantasia = nomefantasia




# henrique = PessoaFisica("henrique", 29)
# mentors = PessoaJuridica("Mentors")

# print(henrique)
# print(mentors)