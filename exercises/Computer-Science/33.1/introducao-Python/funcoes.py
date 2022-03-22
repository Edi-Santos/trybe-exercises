# Funções
# As funções no Python são declaradas iniciando pela palavra reservada
# "def" e delimitadas por : e indentação
def soma(x, y):
    return x + y


print("\nFunções:")
# Podemos passar os parâmetros de forma posicional ou nomeada
print(f"\nPassando parâmetros de forma posicional: {soma(2, 2)}")  # Forma
# posicional

print(f"Passando parâmetro de forma nomeada: {soma(x=2, y=2)}")  # Forma
# nomeada


# Os parâmetros podem ser variádicos, ou seja, podem variar em sua quantidade.
# Parâmetros posicionais variádicos são acessados como tuplas no interior de
# uma função e parâmetros nomeados variádicos como dicionário.

def concat(*strings):
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ", "
    return final_string


to_print_concat = concat("Carlos", "João", "Botaro")
print(f"Parâmetros variádicos: {to_print_concat}")
