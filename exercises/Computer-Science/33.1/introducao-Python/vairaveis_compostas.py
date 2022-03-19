# Funcionalidades para trabalhar com listas (arrays)
fruits = ["orange", "apple", "grape", "pineapple"]  # uma lista em Python

print(f"\nAcessando um elemento: {fruits[0]}")
print(f"Acessando elemento pelo índice negativo: {fruits[-1]}")

fruits.append("banana")  # adicionando novo elemento
print(f"Elemento novo adicionado: {fruits}")

fruits.remove("pineapple")  # removendo um elemento
print(f"Elemento removido: {fruits}")

otherFruits = ["pear", "melon", "kiwi"]
fruits.extend(otherFruits)  # acrescenta nova lista à original
print(f"Acrescentando uma lista nova à lista original: {fruits}")

indice = fruits.index("apple")  # retorna o índice do elemento
print(f"Índice do elemento 'apple': {indice}")

orderdList = sorted(fruits)  # cria um novo objeto ordenado com os elementos
# de uma lista
print(f"Criando novo objeto e ordenando: {orderdList}")

fruits.sort()  # ordena a lista original alterando-a diretamente
print(f"Ordenando lista: {fruits}")
