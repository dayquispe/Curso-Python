# Laços de repetições parte 3

cont = 1
while cont <= 10:
    print(cont, "-> ", end="")
    cont += 1
print("CABO")


n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n

print(f"A soma vale {s}")