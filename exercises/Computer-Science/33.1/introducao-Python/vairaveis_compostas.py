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


# Conjuntos imutáveis(frozenset) - é uma variação do set, porém imutável,
# ou seja, seu elementos não podem ser modificados durante a execução.
permissions_fst = frozenset(["member", "group"])  # assim como o set, qualquer
# estrutura iterável pode ser utilizada para criar um frozenset
union_fsz = permissions_fst.union({"user"})  # novos conjunstos imutáveis
# podem ser criados à partir do original, mas o mesmo não pode ser modificado
print(f"\nCriando um novo conjunto a partir de \
um conjunto imutável: {union_fsz}")

intersection_fst = permissions_fst.intersection({"user", "member"})  # retorna
# um conjunto resultante da interseção dos conjuntos
print(f"Fazendo a interseção entre conjuntos imutáveis: {intersection_fst}")

difference_fst = permissions_fst.difference({"user"})  # retorna a diferença
# entre dois conjuntos
print(f"Retornando a diferença entre um\
conjunto imutável e outro: {difference_fst}")


# Dicionários(dict) - é a estrutura que associa uma chave a um determinado
# valor. É a representação do tão famoso "objeto" que utilizamos no JavaScript
people_by_id = {1: "Cássio", 2: "João", 3: "Felipe"}  # elementos nos formato
# "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {"Cássio": 1, "João": 2, "Felipe": 3}  # outro exemplo, desta
# vez, usando strings como chaves (ao contraŕio de JS, as aspas duplas são
# obrigatórias)

print(f"\nOs elementos dos 'dicts' são acessados por suas chaves: \
{people_by_id[1]}")  # elementos acessados através de suas chaves

del people_by_id[1]  # os elementos podem ser removidos utilizando a palavara
# reservada "del"
print(f"Elementos são removidos pela palavara reservada 'del': \
{people_by_id}")

print(f"Retornando um conjunto com tuplas contendo chaves e valores de um \
dict: {people_by_id.items()}")


# Exerícios
print("\nExercícios")
info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}
# Exercício 8: O que acontecerá se você tentar acessar o valor da chave
# "personagem" como fazíamos em JavaScript, utilizando object.key?
print("Erro de atributo ao tentar acessar um elemento como no JavaScript \
utilizando object.keys(info[\"personagem\"])")
