from queue import PriorityQueue

for i in range(6, 0, -1):
    print(i)

for i in range(0, 101, 10):
    print(i)

numero = int(input("Digite um número: "))

for i in range(1, numero+1):
    print(i)


inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))

for i in range(inicio, fim+1, passo):
    print(i)

somatorio = 0
for i in range(0, 4):
    numero = int(input("Digite um número: "))
    somatorio += numero

print(f"O somatporio dos nímeros foi: {somatorio}")
