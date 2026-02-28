# Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print("-"*15)
print("LOJA SUPER BARATÃO")
print("-"*15)

total_gasto = 0
produto_custo_mais_1000 = 0
nome_produto_barato = ""
preco_produto_barato = 0

while True:
    nome_produto = input("Nome do Produto: ")
    preco = float(input("Preço: R$"))

    if total_gasto == 0:
        preco_produto_barato = preco

    if preco < preco_produto_barato:
        preco_produto_barato = preco
        nome_produto_barato = nome_produto

    total_gasto += preco
    if preco > 1000:
        produto_custo_mais_1000 += 1

    resposta = input("Quer continuar? [S/N] ").lower().strip()
    if resposta != "s":
        break

print("___________FIM DO PROGRAMA___________")
print(f"O total da compra foi R${total_gasto:.2f}")
print(f"Temos {produto_custo_mais_1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_produto_barato} que custa R${preco_produto_barato:.2f}")