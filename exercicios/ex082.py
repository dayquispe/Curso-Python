# Crie um programa que vai ler vários números e
# colocar em uma lista.
# Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores
# ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas
# geradas.

lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    resposta = input("Quer continuar? [S/N] ").lower()
    if resposta == "n":
        break



lista_pares = []
lista_impares = []

for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f"Lista inteira {lista}")
print(f"Lista de números pares {lista_pares}")
print(f"Lista de números ímpares {lista_impares}")