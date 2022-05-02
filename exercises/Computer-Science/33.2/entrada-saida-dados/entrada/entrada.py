import random

# No Python nós temos a função input() como uma das formas de receber dados.
# Esta função retorna sempre dados do tipo String.

meu_numero = input("Digite um número: ")

print(f"Seu número é {meu_numero}")

# No caso acima, é necessário que converta o tipo da
# entrada de String para núemro

meu_numero_convertido = int(input("Digite o núemro para ser \
convertido para 'int': "))

print(f"Seu número convertido: {meu_numero_convertido}")
print(f"Tipo do seu número: {type(meu_numero_convertido)}\n")


# Criando exemplo prático

# escolhe um número aleatório entre 1 e 10
print("Testando na prática")
guess = ""
random_number = random.randint(1, 10)

# enquanto o usuário não acertar este trecho é repetido
while guess != random_number:
    guess = int(input("Qual o seu palpite? "))
    if guess != random_number:
        print("Errou. Tente novamente.")

print("Acertou! O númera sorteado era:", guess, "\n")
