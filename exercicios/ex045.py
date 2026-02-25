# Crie um programa que faça o computador jogar Jokenpõ com você.
from random import  randint
escolha_jogador = int(input("Escolha sua jogada: \n"
                             "[1] Pedra\n"
                             "[2] Papel\n"
                             "[3] Tesoura\n"
                             "==> "))
escolha_computador = randint(1, 3)

ganhou = "Você GANHOU!"
perdeu = "Você PERDEU !"
empate = "Houve EMPATE!"

if escolha_computador == 1:
    print(f"Computador: Pedra")
    if  escolha_jogador == 1:
        print(f"Você: Pedra\n"
              f"{empate}")
    elif escolha_jogador == 2:
        print(f"Você: Papel\n"
              f"{ganhou}")
    else:
        print(f"Você: Tesoura\n"
              f"{perdeu}")
elif escolha_computador == 2:
    print(f"Computador: Papel")
    if  escolha_jogador == 2:
        print(f"Você: Papel\n"
              f"{empate}")
    elif escolha_jogador == 1:
        print(f"Você: Pedra\n"
              f"{perdeu}")
    else:
        print(f"Você: Tesoura\n"
              f"{ganhou}")
else:
    print(f"Computador: Tesoura")
    if escolha_jogador == 3:
        print(f"Você: Tesoura\n"
              f"{empate}")
    elif escolha_jogador == 2:
        print(f"Você: Papel\n"
              f"{perdeu}")
    else:
        print(f"Você: Pedra\n"
              f"{ganhou}")

