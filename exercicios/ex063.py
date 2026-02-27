# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
# primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

numero = int(input("Digite um número para mostrar a sequencia de Fibonacci: "))

cont = 3
e1 = 0
e2 = 1
print(f"{e1}")
print(f"{e2}")
while cont <= numero:
    e3 = e1 + e2
    print(f"{e3}")
    e1 = e2
    e2 = e3
    cont += 1
