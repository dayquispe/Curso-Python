#  Crie um programa que simule o funcionamento de um caixa
#  eletrônico. No início, pergunte ao usuário qual será o
#  valor a ser sacado (número inteiro) e o programa vai
#  informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20,
# R$10 e R$1.

print("-"*15)
print("BANCO CEV")
print("-"*15)

valor = int(input("Que valor você quer sacar? R$"))

cinquenta = valor // 50
sobro = valor%50

vinte = sobro // 20
sobro = sobro%20

dez = sobro // 10
sobro = sobro%10

um = sobro // 1


if cinquenta > 0:
    print(f"Total de {cinquenta} cédulas de R$50")
if vinte > 0:
    print(f"Total de {vinte} cédulas de R$20")
if dez > 0:
    print(f"Total de {dez} cédulas de R$10")
if um > 0:
    print(f"Total de {um} cédulas de R$1")