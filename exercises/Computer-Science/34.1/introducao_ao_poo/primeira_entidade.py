# Uma entidade é o mesmo que um objeto. Um objeto é uma representação de algo
# do mundo físico para a programação. É algo que tem informações e
# comportamentos.

# Criando o primeiro objeto
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
# Está pronto o nosso objeto/entidade
# Nós usamos a palavra reservada "class" para criarmos nossos objetos que
# devem ser sempre abstratos, algo para ser reaproveitado depois.

meu_user = User("Eren Jaeger", "erendotita@gmail.com", "FrenchFries")  # Aqui
# nós estamos reaproveitando o nosso objeto User para criar um novo usuário e
# atribuindo à variável "meu_user". Sendo assim, nossa variável é um objeto.
print(meu_user)
print(meu_user.name)
print(meu_user.email)
print(meu_user.password)

# Usando termos mais técnicos, nós criamos primeiro a nossa classe (que é algo
# "genérico" para ser reaproveitado depois) e em seguida atribuímos à nossa
# variável um objeto (que é uma entidade específica, neste caso, um usuário
# novo).

# Toda classe capaz de criar objetos deve possuir um método construtor. No
# Python, o método construtor é, sempre, definido com o nome "__init__" logo
# abaixo da declaração da classe. Por trás dos panos, o Python utilizará a sua
# lógica para criar e retornar um objeto.

# class User:
#     def __init__(self, name, email, password):
#         """ Método construtor da classe User. Note que
#         o primeiro parâmetro deve ser o `self`. Isso é
#         uma particularidade de Python, vamos falar mais
#         disso adiante!"""
#         self.name = name
#         self.email = email
#         self.password = password
