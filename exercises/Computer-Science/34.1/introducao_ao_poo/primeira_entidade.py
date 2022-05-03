# Uma entidade é o mesmo que um objeto. Um objeto é uma representação de algo
# do mundo físico para a programação. É algo que tem informações e
# comportamentos

# Criando o primeiro objeto
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password