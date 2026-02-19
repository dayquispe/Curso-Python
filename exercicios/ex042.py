# Refaça o Desafio 035 dos triângulos, acrescentando a verificação do tipo de triângulo será formado:
# Equilátero → todos os lados iguais
# Isósceles → dois lados iguais
# Escaleno → todos os lados diferentes

lados = []

for i in range(1, 4):
    lados.append(int(input(f"Digite o {i}° lado do triângiulo: ")))

if lados[0] + lados[1] >= lados[2] and lados[1] + lados[2] >= lados[0] and lados[0] + lados[2] >= lados[1]:
    if lados[0] != lados[1] and lados[1] != lados[2] and lados[2] != lados[0]:
        print(f"Todos os lados são iguais, é um triângulo ESCALENO")
    elif lados[0] == lados[1] or lados[1] == lados[2] or lados[2] == lados[0]:
        print(f"Dois  lados são iguais, é um triângulo ISÓSILES")
    elif lados[0] == lados[1] == lados[2]:
        print(f"Todos os lados são iguais, é um triângulo EQUILATÉRO")

else:
    print(f"Não é possivel transformar em um triângulo!")