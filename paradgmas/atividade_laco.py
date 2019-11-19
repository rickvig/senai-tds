idades = []
idades.append(10)
idades.append(20)
idades.append(30)
idades.append(40)
idades.append(50)


def verifica_idade(idade_a_verificar):
    print("função verifica_idade:", idade_a_verificar)
    
    if idade_a_verificar > 35:
        mensagem = 'Vá ao médico porque sua idade é: %d' % idade_a_verificar 
        print(mensagem)
    else :
        mensagem = 'Voce não precisa ir ao médico pq sua idade é: %d' % idade_a_verificar 
        print(mensagem)


for idade in idades:
    verifica_idade(idade)


def soma_idades(idades):
    lista_aux = []
    for idade in idades:
        idade_mais_um = idade + 1
        lista_aux.append(idade_mais_um)
    
    return lista_aux

print(soma_idades(idades))