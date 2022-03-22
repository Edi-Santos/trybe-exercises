# Exercícios

# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b


printa_maior_numero = maior_numero(4, 2)
print(f"\nExercício 1 - Printa o maior número: {printa_maior_numero}")
