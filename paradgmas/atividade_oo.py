print('Atividade OO')

class Mamifero():
    mamilos = True
    olhos = True
    nome = ''
    cor = ''

    def __init__(self, nome_parametro, cor_parametro):
        self.nome = nome_parametro
        self.cor = cor_parametro


    def mama(self):
        print('%s está mamando e é %s...' % (self.nome, self.cor))

class Aquatico(Mamifero):
    barbatana = True

    def nada(self):
        print("%s esta nadando" % self.nome)

class Baleia(Aquatico):
    espiraculo = True

    def solta_leite_na_agua(self):
        print("%s esta soltando leite na água" % self.nome)


class Terrestre(Mamifero):
    pernas = True
    pes = True

    def caminha(self):
        print("%s esta caminhando" % self.nome)

class Pessoa(Terrestre):
    conciencia = True

    def fala(self):
        print('%s está falando' % self.nome)

class Cachorro(Terrestre):
    pelo = True
    rabo = True

    def late(self):
        print('Au AU')




def main():
    print('Olá estamos no main')

    cachorra_henrique = Cachorro('Laila', 'cinza')
    print('qual é o nome da cachorra do henrique:', cachorra_henrique.nome)
    print('a laila tem mamilos:', cachorra_henrique.mamilos)
    print('a laila tem olhos:', cachorra_henrique.olhos)
    print(cachorra_henrique.late())
    
    print('Acidente da laila')
    cachorra_henrique.mamilos = False
    cachorra_henrique.olhos = False
    print('a laila tem mamilos e olhos depois do acidente:', cachorra_henrique.mamilos, cachorra_henrique.olhos)
    
    print(cachorra_henrique.mama())

    cachorro_diego = Cachorro("Yuki", 'branco')
    print(cachorro_diego.mama())
    
    cachorro_atalaia = Cachorro("Fofinho", 'branco')
    print(cachorro_atalaia.mama())



main()