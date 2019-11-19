'''
Criar funções que calcula a area das formas:

area_do_quadrado()
area_do_losangulo()
area_do_trapesio()
area_do_triangulo()
area_do_circulo()
'''

def area_do_quadrado(base, altura):
    return base * altura

def area_do_losangulo(largura, altura):
    return (largura * altura) / 2

def area_do_trapesio(base_maior, base_menor, altura):
    return ( (base_maior + base_menor) * altura ) / 2

def area_do_triangulo(base, altura):
    return (base * altura) / 2

def area_do_circulo(raio):
    return 3.14 * (raio ** 2)



print("area_do_quadrado =", area_do_quadrado(base=3, altura=3))
print("area_do_losangulo largura =", area_do_losangulo(largura=3, altura=3))
print("area_do_trapesio =", area_do_trapesio(base_maior=12, base_menor=8, altura=6))
print("area_do_triangulo =", area_do_triangulo(base=3, altura=5))
print("area_do_circulo =", area_do_circulo(raio=45))