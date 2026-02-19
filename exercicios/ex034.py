# Escreva um programa qua pargunte o salário de um
# funcionário e calcule o valor do seu aumento.
# Para salários  superioras a R$1.250,00, calcule um
# aumento da 10%. Para os inferioras ou iguais, o aumanto é de 15%.
from rich import print
salario = float(input("Digite seu salário: "))

if salario > 1250:
    salario_novo = salario + (0.1 * salario)
else:
    salario_novo = salario + (0.15 * salario)

print(f"[green]O seu salário novo é de :dollar: R${salario_novo:.2f}[/]")