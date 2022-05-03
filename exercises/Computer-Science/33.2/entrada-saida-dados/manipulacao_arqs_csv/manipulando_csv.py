import csv  # Assim como o json, o csv também é um módulo que vem embutido

# O módulo csv contém duas principais funções:
# Um leitor ( reader() ) que nos ajuda a ler o conteúdo, já fazendo as
# transformações dos valores para Python;
# E um escritor ( writer() ) para facilitar a escrita nesse formato.

with open("balneabilidade.csv") as file:
    ler_status_praia = csv.reader(file, delimiter=",", quotechar='"')  # o leitor
    # define como dialeto padrão o "excel", que significa dizer que o
    # delimitador de campos será "," e o caractere de citação será aspas duplas
    # ( "" ). É possível modificar estes padrões redefinindos na criação do leitor
    header, *data = ler_status_praia  # esta sintaxe é como o "destructuring"
    # no JavaScript mas tem uma funcionalidade um pouco diferente. Aqui está
    # sendo atribuído as colunas (1ª linha do arquivo csv) à variável header
    # e todo o restante do arquivo (os dados) na variável data.

    # print(data)

# Um leitorde CSV pode ser ( reader() ) pode ser percorrido utilizando o laço
# de repetição for que a cada iteração retorna uma nova linha transforamda em
# lista python com seu respectivos valores.

# Desempacotamento de valores

# A sintaxe usada na linha 13 se chama desempacotamento de valores. Neste caso
# foi usado como um truque para separarmos o cabeçalho do restante dos dados.
# Quando há uma atribuição múltipla e o valor da direita (ler_status_praia) pode
# ser percorrida, o Python entende que deve atribuir cada um dos valores a uma
# variável da esquerda (header, *data), seguindo a ordem.
# Exemplo:

a, b = "cd"
print(a)  # saída: c
print(b)  # saída: b

head, *tail = [1, 2, 3]  # Quando um * está presente no desempacotamento, os
# valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]


# Escrevendo em arquivos CSV
balneabilidade_por_camapnha = {}
with open("balneabilidade.csv") as file:
    ler_status_praia = csv.reader(file, delimiter = ",", quotechar= '"')
    header, *data = ler_status_praia

    # agrupando campanhas e suas respectivas balneabilidades
    for linha in data:  # Percorrendo cada linha do arquivo
        campanha = linha[6]
        balneabilidade = linha[2]

        if campanha not in balneabilidade_por_camapnha:
            balneabilidade_por_camapnha[campanha] = {
                "Própria": 0,
                "Imprópria": 0,
                "Muito Boa": 0,
                "Indisponível": 0,
                "Satisfatória": 0,
            }
        balneabilidade_por_camapnha[campanha][balneabilidade] += 1

with open("report_por_campanha.csv", "w") as file:
    escrevendo = csv.writer(file)  # função para escrever num arquivo que é
    # criado automáticamente caso não exista

    # Escrevendo o cabeçalho primeiro
    headers = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    escrevendo.writerow(headers)

    # Escrevendo as linhas de dados
    for campanha, balneabilidade in balneabilidade_por_camapnha.items():
        # desempacotando os valores de balneabilidade para formar uma linha
        # equivalente a:
        # linha = [campanha]
        # for valor in balneabilidade.values():
        #     row.append(valor)
        linha = [campanha, *balneabilidade.values()]
        escrevendo.writerow(linha)


# Existe ainda o leitor e escritor baseado em dicionários. Sua principal
# vantagem é que, com ele, não precisamos manipular os índices para acessar os
# dados das colunas. Mas, devido a estrutura de dados utilizada, ele tem como
# desvantagem o espaço ocupado em memória, sendo maior que o comum.

# Escrevendo em arquivos CSV usando função DictReader() e DictWriter()
balneabilidade_por_camapnha_dicionarios = {}
with open("balneabilidade.csv") as file:
    ler_status_praia = csv.DictReader(file, delimiter = ",", quotechar = '"')
    # a linha de cabeçalhos é utilizada como chave do dicionário
    # agrupa campanhas e suas respectivas balneabilidades

    for linha in ler_status_praia:
        campanha = linha["numero_boletim"]  # as linhas são dicionários
        balneabilidade = linha["categoria"]

        if campanha not in balneabilidade_por_camapnha_dicionarios:
            balneabilidade_por_camapnha_dicionarios[campanha] = {
                "Própria": 0,
                "Imprópria": 0,
                "Muito Boa": 0,
                "Indisponível": 0,
                "Satisfatória": 0,
            }
        balneabilidade_por_camapnha_dicionarios[campanha][balneabilidade] += 1

with open("report_por_campanha_dicionarios.csv", "w") as file:
    # os valores a serem escritos devem ser dicionários
    header = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    
    # é necessário passar o arquivo e o cabeçalho
    escrevendo = csv.DictWriter(file, fieldnames=header)

    # escrevendo as linhas de dados
    for campanha, balneabilidade in balneabilidade_por_camapnha_dicionarios.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # linha = {"campanha": campanha}
        # for nome, valor in balneabilidade.itom():
        #     linha[nome] = valor
        linha = {"Campanha": campanha, **balneabilidade}
        escrevendo.writerow(linha)

# Ainda que a manipulação de arquivos seja algo trivial, caso precise fazer
# análises de dados, leve em consideração bibliotecas como Pandas, elas foram
# construídas e são mantidas justamente para atender e facilitar este objetivo.

