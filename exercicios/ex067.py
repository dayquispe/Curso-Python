# 💡 Faça um programa que mostre a tabuada
# de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O
# programa será interrompido quando o
# número solicitado for negativo.

while True:
    print("--" * 30)
    valor = int(input("Quer ver a tabuada de qual valor? "))
    print("--" * 30)
    if valor < 0:
        break
    for i in range(1, 11):
        print(f"{valor} X {i} = {valor * i}")

print("Programa de tabuada encerrado!")