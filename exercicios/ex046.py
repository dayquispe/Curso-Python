#Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

from rich import print
print(f"Contagem regressiva para estouro de fogos de artifício.")
for i in range(10, 0, -1):
    print(f"{i}")
    sleep(1)
print(":party_popper::party_popper:")