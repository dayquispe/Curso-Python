# Aprimore o desafio anterior, mostrando no final:

#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#c) O maior valor da segunda linha.

matriz = []
lista =  []
for j in range(0, 3):
    for k in range(0, 3):
        numero = int(input(f"Digite um valor para [{j}, {k}]: "))
        lista.append(numero)
    matriz.append(lista[:])
    lista.clear()

soma_valores_pares = 0
soma_valores_terceira_coluna = 0
valor_maior_segunda_linha = max(matriz[1])

print("===========================================")
for i in matriz:
    soma_valores_terceira_coluna += i[-1]

    for j in i:
        print(f"[ {j} ]", end='')
        if j%2 == 0:
            soma_valores_pares+=j
    print("\n", end='')

print("===========================================")
print(f"A soma dos valores pares é {soma_valores_pares}")
print(f"A soma dos valores da terceira coluna é {soma_valores_terceira_coluna}")
print(f"O maior valor da segunda linha é {valor_maior_segunda_linha}")
