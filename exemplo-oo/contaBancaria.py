class ContaBancaria(object):
    saldo = 0

    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def consultaSaldo(self):
        return print("Seu saldo é: " + str(self.saldo))