# Exercício 1 -  Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical. Exemplo:
# F
# U
# L
# A
# N
# O

print("Exercício 1")
nome = input("Digite seu nome: ")

for letra in nome:
    print(letra, "\n")


# Exercício 2 - Escreva um programa que receba vários números naturais e
# calcule a soma desses valores. Caso algum valor da entrada seja inválido,
# por exemplo uma letra, uma mensagem deve ser exibida, na saída de erros,
# no seguinte formato: "Erro ao somar valores, {valor} é um valor inválido".
# Ao final, você deve imprimir a soma dos valores válidos.

print("Exercício 2")

digitos = input("Digite, separando por espaços, números a serem somados: ")
lista_numeros = digitos.split()
soma = 0
err = False
numero_invalido = ''

for numero in lista_numeros:
    verifica_digito = numero.isdigit()

    if verifica_digito:
        numero_convertido = int(numero)
        soma += numero_convertido
    else:
        err = True
        numero_invalido = numero

if err:
    print(f"Erro ao somar valores, \"{numero_invalido}\" é um valor inválido")
else:
    print(f"A soma é: {soma}")
