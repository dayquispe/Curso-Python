# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
from os import remove

lista = []
lista_ordenada = []
for i in range(0, 5):
    numero = int(input("Digite um valor: "))
    lista.append(numero)

for i in range(0, 5):
    lista_ordenada.insert(i, (min(lista)))
    lista.remove(min(lista))

print(lista_ordenada)


