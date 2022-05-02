# Para a saída de dados nós temos como principal a função print()
# Funciona como o console.log() do JavaScript

print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42

# Podemos fazer algumas modificações em seu comportamento
# como, por exemplo, mudar o separador dos argumentos passados
# que, por padrão, é um espaço vazio.

print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída:
# Maria, João, Miguel, Ana

# Podemos também alterar o caractere de fim de linha que, por padrão, é
# uma quebra de linha.

print("Em duas ")
print("linhas.")
# saída:
# Em duas
# linhas.

print("Na mesma", end="")
print("linha.")
# saída:
# Na mesma linha.

# Formatações para saída
x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores,
# como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos
