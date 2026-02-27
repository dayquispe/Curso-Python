# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 a 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import random
cont = 1
numero_computador = random.randint(1, 10)

numero_jogador = int(input("Advinhe um número de 0 á 10: "))

if numero_jogador == numero_computador:
    print(f"Parabéns você adivinhou o número!")
else:
    while numero_computador != numero_jogador:
        numero_jogador = int(input("Tente outro número: "))
        cont +=1
    print(f"Parabéns você adivinhou o número!")
print(f"Quantidade de tentativas: {cont}")