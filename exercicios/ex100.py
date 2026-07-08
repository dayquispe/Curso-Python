# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro de uma lista e  a segunda função vai mostrar a
#soma entre todos os valores PARES sorteados pela função anterior.
from random import  randint

def sorteio():
    lista_sorteados = list()
    print(f"Sorteando 5 valores da lista: ", end="")
    for i in range(0, 5):
        numero_random = randint(0, 10)
        print(f"{numero_random} ", end="")
        lista_sorteados.append(numero_random)
    print()
    return  lista_sorteados

def soma_par():
    lista = sorteio()
    soma = 0
    for num in lista:
        if num %2 == 0:
            soma+=num

    print(f"Somado os valores pares de {lista}, temos {soma}")

soma_par()
