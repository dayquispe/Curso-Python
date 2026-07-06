# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
#ordem, sabendo que o vencedor tirou o maior número no dado.
from random import  randint
from time import sleep
from operator import  itemgetter

jogador = 1
dicionario_numeros = dict()
ranking = list()

print('Valores sorteados')

while True:
    numero = randint(1, 6)
    dicionario_numeros[jogador] = numero
    print(f"   O jogador{jogador} tirou {numero}")
    sleep(1)

    jogador+=1
    if jogador == 5:
        break

ranking = sorted(dicionario_numeros.items(), key=itemgetter(1), reverse=True)

print(" == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}.")
    sleep(1)
