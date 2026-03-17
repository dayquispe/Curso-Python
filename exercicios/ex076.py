# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

tupla = ("caderno", 45, "lápis", 4, "borracha", 56,  "caneta", 4, "livro", 49)
print("___________________")
print("Listagem de preços")
print("___________________")

for i in range(0, len(tupla)):
    if i  % 2 == 0:
        print(f"{tupla[i]} .....................", end=" ")
    else:
        print(f"R${tupla[i]:.2f}")