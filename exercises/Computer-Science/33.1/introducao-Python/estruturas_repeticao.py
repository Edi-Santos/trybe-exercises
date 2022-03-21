# Estruturas de repetição
# No Python nós temos o "for" e o "while". O for é como o for/in do JavaScript


# Percorrer uma lista de restaurantes de acordo com a nota buscada
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
print(f"\nLista de restaurantes com nota acima de 3.0: \
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
