# Crie um programa que faça o computador jogar Jokenpõ com você.
from random import  randint
escolha_jogador = int(input("Escolha sua jogada: \n"
                             "[1] Pedra\n"
                             "[2] Papel\n"
                             "[3] Tesoura\n"
                             "==> "))
escolha_computador = randint(1, 3)

if escolha_computador == 1:
    print(f"Computador: Pedra")
    if  escolha_jogador == 1:
        print(f"Você: Pedra\n"
              f"EMPATE!")
    if escolha_jogador == 2:
        print(f"Você: Papel\n"
              f"Você GANHOU!")
    if escolha_jogador == 3:
        print(f"Você: Tesoura\n"
              f"Você PERDEU!")
elif escolha_computador == 2:
    print(f"Computador: Papel")
    if  escolha_jogador == 2:
        print(f"Você: Papel\n"
              f"EMPATE!")
    if escolha_jogador == 1:
        print(f"Você: Pedra\n"
              f"Você PERDEU!")
    if escolha_jogador == 3:
        print(f"Você: Tesoura\n"
              f"Você GANHOU!")
else:
    print(f"Computador: Tesoura")
    if escolha_jogador == 3:
        print(f"Você: Tesoura\n"
              f"EMPATE!")
    if escolha_jogador == 2:
        print(f"Você: Papel\n"
              f"Você PERDEU!")
    if escolha_jogador == 1:
        print(f"Você: Pedra\n"
              f"Você GANHOU!")

