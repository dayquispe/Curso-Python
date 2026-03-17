# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.



n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

tupla = (n1, n2, n3, n4)

total_nove = tupla.count(9)
print(f"O valor 9 apareceu {total_nove} vezes")

if 9 in tupla:
    posicao = tupla.index(9)
    print(f"A posição do primeiro index do 3 é  {posicao}.")
else:
    print(f"O valor 3 não foi digitado em nenhuma posição")



print("Os valores pares digitados foram:", end=" ")
for n in tupla:

    if  n % 2 == 0:
        print(n, end=" ")



