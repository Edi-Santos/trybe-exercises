# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas,
# escreva um programa que lê todas essas informações e filtre mantendo
# somente as pessoas que estão reprovadas, e escreva seus nomes em outro
# arquivo. A nota miníma para aprovação é 6.

print("Exercício 3")

with open("exercicio_manipulando_arq.txt", mode="w") as arquivo:
    LINHAS = ["Marcos 10\n", "Felipe 4\n", "José 6\n", "Ana 10\n" "Miguel 5\n"]
    arquivo.writelines(LINHAS)


with open("exercicio_manipulando_arq.txt", mode="r") as arquivo:
    reprovados = []

    for linha in arquivo:
        aluno = linha
        aluno = aluno.split()

        if int(aluno[1]) < 6:
            reprovados.append(aluno[0])

    print(reprovados)
