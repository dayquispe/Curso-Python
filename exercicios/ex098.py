# Faça um programa que tenha uma função chamada contador(), que
# recebe três parâmetros:inicio, fim, e passo e realiza a contagem.
#Seu programa tem que realizar três contagens através da função criada:

#a) De 1 até 10, de 1 em 1
#b) De 10 até 0, de 2 em 2
#c) Uma contagem personalizaada

from time import sleep
def deco():
    print("-=" * 20)

def contador(inicio, fim, passo):
    deco()
    print(f"Contagem de 1 até 10 de 1 em 1 ")
    for i in range(1, 11):
        print(f"{i} ", end="")
    print("FIM!")
    deco()

    print(f"Contagem de 10 até 0 de 2 em 2 ")
    for i in range(10, -1, -2):
        print(f"{i} ", end="")
    print("FIM!")
    deco()

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo} ")
    if passo < 0:
        passo *= -1

    if passo == 0 :
        passo = 1
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f"{i} ", end="", flush=True)
            sleep(1)
        print("FIM!")
    else:
        for i in range(inicio, fim-1, -passo):
            print(f"{i} ", end="", flush=True)
            sleep(1)
        print("FIM!")
    deco()

inicio_recebido = int(input("Inicio: "))
fim_recebio = int(input("Fim: "))
passo_recebido = int(input("Passo: "))

contador(inicio_recebido, fim_recebio, passo_recebido)
