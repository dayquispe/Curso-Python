# Crie um programa onde o usuário possa digitar sete valores
#númericos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final mostre os
#valorea pares e ímpares em ordem crescente.

lista_de_listas = [[], []]

for i in range(1, 8):
    valor = int(input(f"Digite o {i}° valor: "))
    if valor % 2 == 0:
        lista_de_listas[0].append(valor)
    else:
        lista_de_listas[1].append(valor)

lista_de_listas[0].sort()
lista_de_listas[1].sort()

print(f"Os valores pares digitados foram: {lista_de_listas[0]}")
print(f"Os valores ímpares digitados foram: {lista_de_listas[1]}")
