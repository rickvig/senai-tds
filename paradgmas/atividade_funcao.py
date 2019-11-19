print('Atividade Paradgma estrutura - Função')


print('potencia com for')

def potencia(a, b):
    valor = 1
    
    for i in range(b):
        valor = valor * a
    
    return valor




potencia_de_2_elevado_a_3 = potencia(2, 3)
print(potencia_de_2_elevado_a_3)

potencia_de_17_elevado_a_2 = potencia(17, 2)
print(potencia_de_17_elevado_a_2)



print('potencia com while')

def potencia_while(a, b):
    i = 1
    valor = 1
    
    while i <= b:
        valor = valor * a
        i += 1
    
    return valor


potencia_de_2_elevado_a_3 = potencia_while(2, 3)
print(potencia_de_2_elevado_a_3)

potencia_de_17_elevado_a_2 = potencia_while(17, 2)
print(potencia_de_17_elevado_a_2)




print('potencia com python')

def potencia_python(a, b):
    return a ** b


potencia_de_2_elevado_a_3 = potencia_python(2, 3)
print(potencia_de_2_elevado_a_3)

potencia_de_17_elevado_a_2 = potencia_python(17, 2)
print(potencia_de_17_elevado_a_2)



