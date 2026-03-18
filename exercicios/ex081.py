# Crie um programa que vai ler vários números e
# colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
from pickle import TRUE

lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    resposta = input("Quer continuar? [S/N]").lower().strip()
    if resposta == "n":
        break

lista.sort(reverse=True)

print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são {lista}")
print(f"O valor 5 {"não faz" if 5 not in lista else "faz"} parte da lista!")



