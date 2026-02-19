# Faça um programa que leia três números e mostre qual é maior e qual menor
numeros = []
for i in range(1, 4):
    numeros.append(int(input(f"Digite o {i}° número: ")))

print(f"O menor número é {min(numeros)}\nO maior número é {max(numeros)}.")