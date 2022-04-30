# Em Python temos a função open() para abrir e manipular um arquivo seka
# escrevendo, lendo ou os dois.
# Seu único parâmetro obrigatório é o primeiro que é o nome do arquivo.
# Por padrão os arquivos são abertos apenas para leitura mas podemos alterar
# passando o parâmetro "mode='w'" com o valor "w", por exemplo.

file = open("arquivo.txt", mode="w")  # ao abrir um arquivo para escrita, um
# novo arquivo é criado mesmo que ele já exista, sobrescrevendo o antigo.

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")
# Podemos escrever num arquivo apenas após o abrirmos.

# Podemos escrever ainda usando o print() redirecionando sua saída para o
# arquivo a ser manipulado.

# Não precisa da quebra de linha, pois esse é um comportamento padrão do print
print("Túlio 22", file=file)

# Para escrever múltiplas linhas podemos utilizar a função writelines(). Repare
# que a função espera que cada linha tenha seu próprio caractere de separação
# (\n).

LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)

# Feito o que se queria dentro do arquivo, é necessário fechá-lo
file.close()


# Para fazermos a leitura nós temos a função read().

# Escrita
file2 = open("arquivo2.txt", mode="w")
file2.write("Meu pastel é mais barato.")
file2.close()  # fechando o arquivo

# Leitura
file2 = open("arquivo2.txt", mode="r")
content = file2.read()
print(content)
file.close()  # sempre fechando o arquivo


# Um é também um iterável, podendo então, ser percorrido por um array,
# por exemplo.
# escrita
file3 = open("arquivo3.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file3.writelines(LINES)
file3.close()

# leitura
file3 = open("arquivo3.txt", mode="r")
for line in file3:
    print(line)  # não esqueça que a quebra de linha também é um caractere da linha
file3.close()  # não podemos esquecer de fechar o arquivo


# Temos ainda o "with" que é uma palavra reservada para gerenciamento de contexto.
# Aqui acontece um encapsulamento de um recurso garantindo que certas ações sejam
# tomadas independentemente se ocorreu erro ou não naquele contexto.

# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)
