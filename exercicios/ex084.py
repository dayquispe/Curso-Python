# Faça um programa que leia nome e peso de várias pesssoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
pessoa = list()
pessoas_leves = list()
pessoas_pesadas = list()
maior = menor = 0
while True:
    pessoa.append(input("Nome: "))
    pessoa.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()
    resposta = input("Quer continuar? [S/N]: ").lower().strip()
    if resposta in "nãoNãonaoNAO":
        break

print(f"Quantidade de pessoas cadastradas foi {len(pessoas)}")
print(f"O maior peso foi de {maior:.2f}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=" ")

print()

print(f"O menor peso foi de {menor:.2f}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=" ")

