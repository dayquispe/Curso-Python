# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print("10 primeiros termos da PA")
primeiro_termo = int(input("Digite o primeiro termo da razão: "))
razao = int(input("Digite  a razão da PA: "))
monte = primeiro_termo
cont = 1
print(f"{primeiro_termo}", end=" ")
while cont < 10:
    print(f"{monte + razao}", end=" ")
    monte+= razao
    cont += 1
