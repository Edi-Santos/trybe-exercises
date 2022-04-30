# O sistema operacional espera que um programa escreva erros na saída de erros
# Existe um parâmetro que nos permite modificar a saída padrão para a saída de
# erros:

import sys

err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}\n", file=sys.stderr)
