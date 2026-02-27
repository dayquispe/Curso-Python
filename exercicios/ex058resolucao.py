from random import randint
computador = randint(0, 10)
print("Sou seu computador e acabei de pensar em um número!")
print("Tente adivinhar o número")

palpites = 0
acertou = False

while not acertou:
    numero = int(input("Digite um número: "))
    palpites += 1
    if numero == computador:
        acertou = True
    else:
        if numero > computador:
            print("Menos... tente novamente!")
        else:
            print("Mais... tente novamente!")
print("Parabéns você acertou!!")
