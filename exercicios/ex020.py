# O mesmo professor do desafio anterior quer sortear a ordem de apresentação  de trabalhos dos
# alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random

lista_alunos = []
for i in range(1, 5):
    lista_alunos.append(input(f"Digite o nome do {i}° aluno: "))

random.shuffle(lista_alunos)

print(f"A ordem sorteada foi: {lista_alunos}")