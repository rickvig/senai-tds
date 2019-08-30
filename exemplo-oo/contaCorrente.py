from contaBancaria import ContaBancaria
class ContaCorrente(ContaBancaria):
    
    def depositar(self, valor):
        if (valor < 100):
            print('Valor minimo é R$100,00')
            return
        
        super().depositar(valor)