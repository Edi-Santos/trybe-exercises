import json  # json é um módulo que vem embutido, porém precisamos importá-lo

# Os principais métodos do json são:
# load, loads, dump e dumps

# O método "loads" carrega o JSON a partir de um texto enquanto o método load
# carrega o JSON a partir de um arquivo.

# Utilizando o método "loads"
print("Utilizando o método 'loads'")
with open("pokemons.json") as file:
    content = file.read()  # leitura do arquivo
    pokemons = json.loads(content)["results"]  # Aqui nós estamos 
    # desserializando pegando o retorno da leitura do arquivo json e
    # formatando para uma estrutura Python. Neste caso, estamos transformado em
    # dicionários. A chave "results" é onde se encontram os pokemóns

    print(pokemons[0], "\n")

print("Utilizando o método 'load'")
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

    print (pokemons[1], "\n")


# Vimos os métodos "load" e "loads" para leitura de arquivo JSON. Veremos agora
# Os métodos "dump" e "dumps" para escrita em arquivos JSON.

# Utilizando método "dumps"
print("Utilizando o método 'dumps'")
# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

    # separando somente os do tipo grama
    pokemons_tipo_grama = [
        pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
    ]

# Abrind o arquivo para escrevermos apenas os pokemons do tipo grama
with open("pokemons_tipo_grama.json", "w") as file:
    novo_arquivo = json.dumps(pokemons_tipo_grama)  # conversão de Python para
    # o formato JSON (str)
    file.write(novo_arquivo)
# Assim como a desserialização, que faz a transformação de texto em formato
# JSON para Python , a serialização, que é o caminho inverso, também possui um
# método equivalente para escrever em arquivos de forma direta.

print("Utilizando o método 'dump'")
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

    pokemons_tipo_fogo = [
        pokemon for pokemon in pokemons if "Fire" in pokemon["type"]
    ]

with open("pokemons_tipo_fogo.json", "w") as file:
    # Com o 'dump' nós podemos converter para o formato JSON e escrever no
    # arquivo de uma vez só. Primeiro parâmetro é o que será escrito e o
    # segundo é onde será escrito.
    json.dump(pokemons_tipo_fogo, file)
