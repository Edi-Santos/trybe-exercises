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

# Exercício 5: Adicione o elemento "Ciência da Computação" à lista.
trybe_course = ["Introdução", "Front-end", "Back-end"]

print("\nExercício 5")
trybe_course.append("Ciência da Computação")
print(f"Adicionando elemento à lista: {trybe_course}")

# Exercício 6: Acesse e altere o primeiro elemento da lista para "Fundamentos".
print("\nExercício 6")
trybe_course[0] = "Fundamentos"
print(f"Modificando o primeiro elemento da lista: {trybe_course}")


# Tuplas - são similares a listas, porém não podem ser modificados durante
# a exercução do programa
user = ("Cássio", "Botaro", 42)  # elementos são definidos e separados por
# vírgula, envolvidos por parenteses
print(f"\nTuplas são acessadas por índices: {user[0]}")


# Conjuntos(set) - são elementos únicos e não ordenados. Como conjuntos,
# implementam operações de união, intersecção e outras
permissions = {"member", "group"}  # elementos separados por vírgula,
# envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto
print(f"\nAdicionando um novo elemento ao conjunto: {permissions}")

permissions.add("member")
print(f"Como já existe um elemento 'member',\
  não é criado novamente: {permissions}")

unified_sets = permissions.union({"user"})  # retorna um conjunto resultante
# da união de dois conjuntos
print(f"Fazendo a união entre dois conjuntos: {unified_sets}")

intersection_set = permissions.intersection({"user", "member"})  # retorna
# um conjunto resultante da intersecção dos conjuntos
print(f"Fazendo a interseção entre conjuntos: {intersection_set}")

difference = permissions.difference({"user"})  # retorna a diferença entre
# os conjuntos
print(f"Retornando a diferença entre um conjunto e outro: {difference}")
