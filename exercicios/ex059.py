# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
escolha = 1

while escolha != 5:
    n1  = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    escolha = int(input(""" 
        Escolha uma opção:
         
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        ==> 
    """))

    match escolha:
        case 1:
            print(f"A soma entre {n1} e {n2} == {n1 + n2}")
        case 2:
            print(f"A multiplicação entre {n1} e {n2} == {n1 * n2}")
        case 3:
            if n1 > n2:
                print(f"O maior número é {n1}")
            elif n2 > n1:
                print(f" O maior número é {n2}")
            else:
                print("Os números são iguais!")
        case 4:
            print(f"Insira os novos números")

        case 5:
            print("Fim de programa")

        case _:
            print("Número não válido")

