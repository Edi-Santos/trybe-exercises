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
