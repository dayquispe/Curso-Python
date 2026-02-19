# Desenvolva um programa que leia o comprimento de três retas
# e diga ao asuário se elas podem ou não formar um triângulo.
from sys import flags

reta1 = float(input("Digite o tamanho de primeira reta: "))
reta2 = float(input("Digite o tamanho de segunda reta: "))
reta3 = float(input("Digite o tamanho de terceira reta: "))

if reta1 <= reta2 + reta3 and reta2 <= reta1 + reta2 and reta3 <= reta2 + reta1:
    print(f"Sim essas retas podem se transformar em um triângulo: ")
else:
    print(f"Não é possível formar um triângulo com essas retas!")