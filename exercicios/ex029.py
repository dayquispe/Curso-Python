# Escreva um programa que leia a
# velocidade de um carro.
# Se ele ultrapassare 80Km/h, mostre uma
# mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km
# acima do limite.
from rich import print
velocidade_carro = int(input("Digite qual a velocidade do carro: "))
km_acima_limite = velocidade_carro - 80
multa = km_acima_limite * 7

if velocidade_carro > 80:
    print(f"Você foi multado por excesso de velocidade!\n"
          f"Terá que pagar a multa no valor de [red]R${multa:.2f}[/].")
else:
    print(f"Você esta dentro do limite de velocidade.")
