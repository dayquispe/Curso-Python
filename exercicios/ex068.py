#  Faça um programa que jogue par ou
#  impar com o computador. O jogo só
#  será interrompido quando o jogador
#  PERDER, mostrando o total de vitórias
#  consecutivas que ele conquistou no
#  final do jogo.

from random import randint

numero_computador = randint(1, 10)
print("=-" * 15)
print("Vamos jogar Par ou Ímpar")
ganhou = 0
while True:
    print("=-" * 15)
    valor = int(input("Diga um valor: "))
    par_impar = input("Par ou Ímpar? [P/I] ").lower()
    soma = valor + numero_computador
    print(f"Você jogou {valor} e o computador {numero_computador}. Total de {soma} DEU", end=" ")
    if soma % 2 != 0 and par_impar == "p" or soma % 2 == 0 and par_impar == 'i':
        print("PAR" if soma%2==0 else "ÍMPAR")
        print("-" * 30)
        print("Você PERDEU!")
        break
    else:
        print("PAR" if soma % 2 == 0 else "ÍMPAR")
        ganhou += 1
        print("Você VENCEU!")
        print("Vamos jogar novamente...")

if ganhou > 1:
    vez = "vezes"
else:
    vez = "vez"
print(f"GAME OVER! Você venceu {ganhou} {vez}")


