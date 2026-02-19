# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.
import random

lista_alunos = []

for i in range(1, 4):
    lista_alunos.append(input(f"Digite o nome do {i}° aluno: "))

sorteado = random.choice(lista_alunos)

print(f"O aluno sorteado foi: {sorteado}")