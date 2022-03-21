# Estruturas de repetição
# No Python nós temos o "for" e o "while". O for é como o for/in do JavaScript


# Percorrer uma lista de restaurantes de acordo com a nota buscada
print("\nFor")
restaurants = [
  {"name": "Restaurante A", "nota": 4.5},
  {"name": "Restaurante B", "nota": 3.0},
  {"name": "Restaurante C", "nota": 4.2},
  {"name": "Restaurante D", "nota": 2.3},
]

# Filtrando os restaurantes de acordo com a nota
filtered_restaurants = []
min_rating = 3.0

for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(f"Lista de restaurantes com nota acima de 3.0: \
{filtered_restaurants}")

# Outra forma de popular um array quando se precisa filtrar dados de
# outro array é usando a sintaxe de compreensão de listas
filtering_by_other_form = [restaurant_
                           for restaurant_ in restaurants
                           if restaurant_["nota"] > min_rating]
print(f"Mesma lista de cima, porém, usando sintaxe de compreensão de \
listas: {filtering_by_other_form}")

filtered_restaurants_name = [restaurant_name["name"]
                             for restaurant_name in restaurants
                             if restaurant_name["nota"] > min_rating]
print(f"Pegando apenas os nomes dos restaurantes: {filtered_restaurants_name}")


# O while funciona de forma bem parecida com o for usado no JavaScript
# executando um trecho de código enquanto aquela condição for verdadeira
print("\nWhile")
n = 10
last, next = 0, 1  # Atribuição múltipla. Esta é uma forma de atribuir
# valores, na mesma linha, a mais de uma variável
fibancci = []
while last < n:
    fibancci.append(last)
    last, next = next, last + next
print(f"Fibonacci: {fibancci}")


# Exercícios
print("\nExercícios")

# Exercício 13: O Fatorial de um número inteiro é representado pela
# multiplicação de todos os números predecessores maiores que 0. Por exemplo
# o fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5 . Escreva um código que
# calcule o fatorial de um número inteiro.
number = 5
n1 = 1
factors = []
factorial = 1

while n1 <= number:
    factors.append(n1)
    n1 += 1

for factor in factors:
    factorial = factorial * factor
print(f"Exercício 13 - Fatorial de {number}: {factorial}")

# Exercício 14: Um sistema de avaliações registra valores de 0 a 10 para cada
# avaliação. Após algumas mudanças estes valores precisam ser ajustados para
# avaliações de 0 a 100. Dado uma sequência de avaliações
# ratings = [6, 8, 5, 9, 10]. Escreva um código capaz de gerar as avaliações
# após a mudança. Neste caso o resultado deveria ser [60, 80, 50, 90, 100].
ratings = [6, 8, 5, 9, 10]
acc = 0

for rating in ratings:
    ratings[acc] = rating * 10
    acc += 1
print(f"Exercício 14 - Alterando os valeres de uma lista de avaliações: \
{ratings}")
