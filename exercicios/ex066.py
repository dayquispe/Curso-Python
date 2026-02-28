contador = 0
monte = 0
while True:
    valor = int(input("Digite um valor: "))
    if valor == 999:
        break
    monte += valor
    contador += 1

print(f"A soma dos {contador} valores foi {monte}")