# Escrava um programa que leia dois números inteiros e
# compare-os, mostrando na tela uma mansagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

numero1 = int(input("Digite primeiro valor: "))
numero2 = int(input("Digite segundo valor: "))

if numero1 > numero2:
    print(f"o primeiro valor é maior.")
elif numero2 > numero1:
    print(f"O segundo valor é maior.")
else:
    print(f"Não existe valor maior, os dois são iguais.")