# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = 0
menor = 0
acumula = 0
cont = 0
while True:
    numero = int(input("Digite um número: "))
    if cont == 0:
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    acumula += numero
    cont += 1

    resposta = str(input("Você quer continuar? ")).lower().strip()
    if resposta == "sim":
        pass
    else:
        break

media = acumula / cont

if maior == menor:
    print("Os numeros são uguais!")
else:
    print(f"O maior número {maior}\n"
          f"O menor número é {menor}")

print(f"A média dos números é {media}")