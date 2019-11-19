from pessoa import Pessoa
from pessoa.pessoaFisica import PessoaFisica
from pessoa.pessoaJuridica import PessoaJuridica

pessoa = Pessoa("Henrique", "(44) 99941-0923")
# print(pessoa)

pessoa2 = PessoaFisica("Lorena", 27)
pessoa2.telefone = '9999999999'

# print(pessoa2)


pessoa3 = PessoaJuridica("Mentors", "00001/12345566")
pessoa3.nome = "Empresa mentors"
pessoa3.telefone = "(44) 123-12312"
# print(pessoa3)



##### Conta Bancaria ####

from contaBancaria import ContaBancaria
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

conta1 = ContaBancaria(10)
conta1.depositar(1000)
conta1.consultaSaldo()

conta1.sacar(500)
conta1.consultaSaldo()

conta2 = ContaCorrente(100)
conta2.depositar(101)
conta2.consultaSaldo()

conta2.depositar(99)
conta2.consultaSaldo()

conta3 = ContaPoupanca()
conta3.consultaSaldo()
conta3.depositar(50)
conta3.rentabilidade()
conta3.consultaSaldo()

print('\n\n')
saldo_total = 0
for conta in [conta1, conta2, conta3]:
    conta.consultaSaldo();
    saldo_total += conta.saldo
    
print(saldo_total)