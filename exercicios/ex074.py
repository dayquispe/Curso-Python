#Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint

tupla_numeros = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))
print(f"Números na tupla: {tupla_numeros}")
menor = tupla_numeros[0]
maior = tupla_numeros[0]
for i in tupla_numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i 

print(f"Maior número é: {maior}")
print(f"Menor número é: {menor}")


