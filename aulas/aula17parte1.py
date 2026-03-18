lanches = ["Hamburgers", "suco", "pizza", "pudim"]

# lanche.append("bala") - adiciona no final da lista
# lanche.insert(0, "hot dog") - adiciona na posição 0, o python refaz a numeração dos indices!

# Como apagar?
# del lanche[3] - delata o que estiver na posição 3, e reposiciona os indices.
# lanche.pop(3) - sem parametro algum apaga o último elemento da lista, ou se não uma posicão especifica
# lanche.remove("pizza") - apaga pelo conteúdo

valores = list(range(4, 11))
print(valores)

outros_valores = [4, 6, 3, 6, 3, 5, 4]
outros_valores.sort() # Ordena os valores!!
print(outros_valores)

outros_valores.sort(reverse=True) # Ordena os valores do maior para o menor
print(outros_valores)


print("Praticando")

num = [2, 2, 2, 111, 2, 6, 2]
num[2] = 54
num.append(32)
print(f"Primeira mudança: {num}")

num.sort(reverse=True)
num.insert(0, 111)
num.pop()
num.pop()
print(f"Segunda mudança: {num}")

num.remove(2) # Ele
print(f"Terceira mudança: {num}") # Remove o primeiro 2 que ele encontra

if 111 in num:
    num.remove(111)
else:
    print("Não achei o número 4")
print(num)

for i, v in enumerate(num):
    print(f"na posição {i} encontrei o valor {v}")
print('_' * 30)

a = [2, 3, 4, 7]
b = a # ligação de uma lista com a outra
b[2] = 8
print(f"Lista a = {a}")
print(f"Lista b = {b}")

print(a[2])
print(b[2])

c = [2, 3, 4, 7]
d = c[:] # d recebe cópia de c
d[2] = 8
print(f"Lista c = {c}")
print(f"Lista d = {d}")
print(c[2])
print(d[2])