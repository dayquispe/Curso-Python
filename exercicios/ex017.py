# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa
from rich import print
import math
from math import pow, sqrt
cateto_oposto = float(input("Digite em centimentro o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite em centimentro o comprimento do cateto adjacente: "))
hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

print(f"A hipotenusa de triângulo retângulo :triangular_ruler: é {hipotenusa:.2f}")