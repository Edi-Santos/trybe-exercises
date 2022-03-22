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

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo
# a quantidade de latas de tinta a serem compradas e o preço total a partir
# do tamanho de uma parede(em m²).


def tinta_para_metros(metros):
    metro_lata = 58
    preco_lata = 80.00
    quantidade_latas = 0
    preco_total = 0

    if metros <= metro_lata:
        quantidade_latas = 1
    else:
        quantidade_latas = metros // metro_lata + 1
        preco_total = preco_lata * quantidade_latas

    return (quantidade_latas, preco_total)


print(f"Exercpicio 5 - Quantidade de latas e preço total: \
{tinta_para_metros(80)}")

# Exercício 6: Crie uma função que receba os três lados de um triângulo e
# informe qual o tipo de triângulo formado ou "não é triangulo" , caso não
# seja possível formar um triângulo.


def tipo_triangulo(ladoA, ladoB, ladoC):
    triangulo = (
        ladoA + ladoB > ladoC and
        ladoB + ladoC > ladoA and
        ladoC + ladoA > ladoB
    )

    if not triangulo:
        return "Não é triângulo"
    elif ladoA == ladoB == ladoC:
        return "Triângulo equilátero"
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        return "Triângulo isósceles"
    else:
        return "Triângulo escaleno"


print(f"Exerício 6 - Tipo de triângulo: {tipo_triangulo(5, 9, 5)}")
