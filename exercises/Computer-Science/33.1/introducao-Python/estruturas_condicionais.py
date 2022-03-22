# Estruturas condicionais
# No Python não existe switch/case, apenas if/elif/else


# Atribuindo um cargo à uma variável de acordo com o salário
position = ""
salary = 4700

if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "senior"
elif 7500 < salary <= 10500:
    position = "pleno"
else:
    position = "líder"

# No Python não se usa {} para delimitar blocos de código e sim : e a
# identação. A identação padrão é de 4 espaços.

print("\nUsando estrutura condicional:")
print(f"\nCargo: {position} - Salário R$ {salary:,.2f}")
