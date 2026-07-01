# Faça um programa que ajude um jogador da Mega Sena a criar
#palpite. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.

from random import randint
from time import sleep

print("________________")
print("JOGO NA MEGA SENA")
print("________________")

numeros_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"=-=-=-=- Sorteando {numeros_jogos} jogos -=-=-=-=")
lista_numeros_sorteados = []
for i in range(0, numeros_jogos):
    while len(lista_numeros_sorteados) < 6:
        numero_random = randint(1, 60)
        if numero_random not in lista_numeros_sorteados:
            lista_numeros_sorteados.append(numero_random)
    lista_numeros_sorteados.sort()
    print(f"JOGO {i+1}: {lista_numeros_sorteados[:]}")
    sleep(1)
    lista_numeros_sorteados.clear()
