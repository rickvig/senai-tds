print('Aula de Paradgma estruturado')

# váriavel numérica
idade = 30
print(idade)

# váriavel de texto
nome = 'Henrique'
print(nome)

# váriavel boolean
status = True
print(status)


lista_idades = []
print(lista_idades)
lista_idades.append(idade)
lista_idades.append(45)
lista_idades.append(55)
print(lista_idades)
print(lista_idades[1])

print("##################")
for elemento in lista_idades:
    print(elemento)


def verifica_idade(idade_a_verificar):
    print("função verifica_idade:", idade_a_verificar)
    
    if idade_a_verificar > 55:
        mensagem = 'Vá ao médico porque sua idade é: %d' % idade_a_verificar 
        print(mensagem)
    else :
        mensagem = 'Voce não precisa ir ao médico pq sua idade é: %d' % idade_a_verificar 
        print(mensagem)

verifica_idade(67)

# declaração da função
def soma_idade(idade1, idade2):
    return idade1 + idade2


# invocação da função
soma_das_idades = soma_idade(15, 55)

print(soma_das_idades)