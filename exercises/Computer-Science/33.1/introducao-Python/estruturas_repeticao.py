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
