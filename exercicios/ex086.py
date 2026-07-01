# Crie um programa que crie uma matriz
#de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = []
lista =  []
for j in range(0, 3):
    for k in range(0, 3):
        numero = int(input(f"Digite um valor para [{j}, {k}]: "))
        lista.append(numero)
    matriz.append(lista[:])
    lista.clear()
print(matriz)

for i in matriz:
    for j in i:
        print(f"[{j:^5}]", end='')
    print("\n", end="")
