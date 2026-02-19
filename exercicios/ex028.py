# Escreva um programa que faça o computador
# 'pensar' em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
from rich import print
import random

numero_computador = random.randint(0, 5)

print(f"*" * 12)
print(":thinking_face:[green] Adivinhe o numero que eu estou pensando, \n"
      "o número está entre 0 e 5: [/]", end=" ")
numero_jogador = int(input(""))
print(f"*" * 12)

if numero_computador == numero_jogador:
    print(f"Parabéns você adivinhou!:+1:")
else:
    print("Você Errou!! :-1:")
