# Exercício 1: No terminal, inicializa duas variáveis a e b,
# sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas
# (soma, subtração, multiplicação, divisão, divisão inteira,
# potenciação e módulo) envolvendo essas variáveis.
a = 10
b = 5

print("\nExercício 1")
print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Potenciação:", a ** b)
print("Módulo", a % b)

# Exercício 2: Declare e inicialize uma variável: hours = 6 . Quantos minutos
# têm em 6 horas? E quantos segundos? Declare e inicialize
# variáveis minutes e seconds que recebem os respectivos resultados
# das contas. Depois, imprima cada uma delas.
hours = 6
minutes = hours * 60
seconds = minutes * 60

print("\nExercício 2")
print("Horas:", hours)
print("Minutos:", minutes)
print("Segundos:", seconds)

# Exercício 3: Teste e verifique o que acontece se você colocar um ponto e
# vírgula no final de uma instrução em Python.
testing = "Meu pastel é mais barato"

print("\nExercício 3")
print("Testando ponto e vírgula ao final de uma instrução ---", testing)
print("Aqui nós temos um erro de sintaxe pois o \
  Python não exige ; ao final de suas instruções")

# Exercício 4: Suponha que o preço de capa de um livro seja 24,20, mas
# as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o
# primeiro exemplar e 75 centavos para cada exemplar adicional.
# Qual é o custo total de atacado para 60 cópias? Escreva uma expressão
# que receba o custo total e a imprima.
custoCapaLivro = 24.20
descontoLivraria = custoCapaLivro - (custoCapaLivro * 40 / 100)
custoTransporte = 0.75 * 59 + 3.00
custoTotal = descontoLivraria + custoTransporte

print("\nExerício 4")
print(f"Custo total de atacado para 60 cópias de livros: R$ {custoTotal:,.2f}")
