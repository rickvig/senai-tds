from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJurdica

pessoa = Pessoa("Henrique", "(44) 99941-0923")
# print(pessoa)

pessoa2 = PessoaFisica("Lorena", 27)
pessoa2.telefone = '9999999999'

# print(pessoa2)


pessoa3 = PessoaJurdica("Mentors", "00001/12345566")
pessoa3.nome = "Empresa mentors"
pessoa3.telefone = "(44) 123-12312"
# print(pessoa3)



##### Conta Bancaria ####

from contaBancaria import ContaBancaria
from contaCorrente import ContaCorrente

conta1 = ContaBancaria(10)
conta1.depositar(1000)
conta1.consultaSaldo()

conta1.sacar(500)
conta1.consultaSaldo()

conta2 = ContaCorrente(100)
conta2.depositar(101)
conta2.consultaSaldo()