from contaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    rentabilidade_total = 1.6

    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        return super().depositar(valor)
    
    def rentabilidade(self):
        self.saldo = (self.saldo * self._consulta_rentabilidade()) + self.saldo
        return print("Sua rentabilidade é {0}%, seu saldo atual é {1}".format(self.rentabilidade_total, self.saldo))
    
    def _consulta_rentabilidade(self):
        return (self.rentabilidade_total / 100)