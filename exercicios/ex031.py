# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrada R$0,50 por Km para viagens
# de até 200Km e R$0.45 para viagens mais longas.
from rich import print
distancia = float(input("Digite a distância percorrida em Km: "))

if distancia <= 200:
    print(f"Sua passagem custa: :dollar: R${distancia * 0.50:.2f}")
else:
    print(f"Sua passagem custa: :dollar: R${distancia * 0.45:.2f}")
