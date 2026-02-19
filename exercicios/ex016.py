# Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela a sua porção Inteira.
#ex: Digite um número 12.33
# O número 12.33 tem a parte inteira 12.
from math import trunc
numero_real = float(input("Digite um número qualquer: "))
print(f"O número digitado foi {numero_real}.\nA parte inteira dele é {trunc(numero_real)}.")