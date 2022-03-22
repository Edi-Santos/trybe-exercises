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

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
print("Exercício 3 - Imprimindo quadrado de '*' dado um 'n' valor")
n3 = 5

if n3 > 1:
    n3_list = range(n3)
    for number3 in n3_list:
        print("*" * n3)

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome
# com a maior quantidade de caracteres. Por exemplo, para
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"],
# o retorno deve ser "Fernanda".
lista_nomes = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
maior_nome = ""

for nome in lista_nomes:
    if len(maior_nome) < len(nome):
        maior_nome = nome
print(f"Exercício 4 - Imprimindo o maior nome da lista: {maior_nome}")
