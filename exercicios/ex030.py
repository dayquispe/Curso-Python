# Crie um progarma qu eleia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR
from rich import print
numero = int(input("Digite um número qualquer para ver se ele é par ou ímpar: "))

if numero % 2 == 0:
    print(f"O número é [bold blue]PAR[/]!")
else:
    print(f"O número é [bold blue]ÍMPAR[/]!")


