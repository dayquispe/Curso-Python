# Cria um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

nome_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
                    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis",
                    "dezessete", "dezoito", "dezenove", "vinte")

while True:
    numero = int(input("Digite um número ente 0 e 20: "))
    if numero not in range(0, len(nome_por_extenso)):
        print(f"Tente novamente. Digite um número entre 0 e 20: ")
        pass
    else:
        print(f"Você digitou o número {nome_por_extenso[numero]}")
        break
