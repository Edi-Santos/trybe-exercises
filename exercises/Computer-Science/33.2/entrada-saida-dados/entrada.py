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
