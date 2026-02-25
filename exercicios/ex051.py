# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

numero_final = primeiro_termo*razao*10

for i in range(primeiro_termo,numero_final+1, razao ):
    print(f"{i}")