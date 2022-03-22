# Exercícios

# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b


printa_maior_numero = maior_numero(4, 2)
print(f"\nExercício 1 - Printa o maior número: {printa_maior_numero}")

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
lista_numeros = [3, 4, 6, 8, 10, 5]
tamanho_lista = len(lista_numeros)
soma_numeros = 0

for numero in lista_numeros:
    soma_numeros += numero

media = soma_numeros / tamanho_lista
print(f"Exercício 2 - Calcula a média de uma lista: {media}")
