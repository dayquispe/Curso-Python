# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada
# um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []

resposta = 'sim'
while resposta == "sim":
    nome = input("Nome: ")
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2)/2
    lista.append([nome, nota_1, nota_2, media])

    resposta = input("Quer continuar? [S/N] ").lower().strip()
    if resposta == 'não':
        break

print(f"{'No.':<4} {'NOME':<10}{'MÉDIA':>8}")
print("---------------------------")
cont = 0
for aluno in lista:
    print(f"{cont:<4}    {aluno[0]:<10}     {aluno[3]:>8.1f}")
    cont += 1

while True:
    resposta_numero = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if resposta_numero in range(0, len(lista)):
        print(f"Notas de {lista[resposta_numero][0]} são {lista[resposta_numero][1:3]}")

    if resposta_numero == 999:
        break
