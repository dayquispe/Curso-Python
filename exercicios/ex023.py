# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separdos.

#ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
from rich import print
numero = int(input("Digite um número entre 0 a 9999: "))

unidade = numero % 10
dezena = numero % 100 // 10
centena = numero % 1000 // 100
milhar = numero % 10000 // 1000

print(f"[blue]Digitos separados:[/] \n"
      f"[green]Unidade: {unidade}\n"
      f"Dezena: {dezena}\n"
      f"Centena: {centena}\n"
      f"Milhar: {milhar}")

print(10%3)
print(10//3)

#Resolução:

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 100 % 10

print(f"[blue]Digitos separados:[/] \n"
      f"[green]Unidade: {u}\n"
      f"Dezena: {d}\n"
      f"Centena: {c}\n"
      f"Milhar: {m}")