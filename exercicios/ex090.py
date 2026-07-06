# Faça um programa que leia nome e média de um aluno, guardando
#também a situação em um dicionário. no final, mostre o conteúdo
#estrutura na tela.

lista_de_alunos = list()
aluno = dict()

while True:
    aluno['nome'] = str(input("Nome: "))
    aluno['media_nota'] = float(input(f"Média de {aluno['nome']}: "))

    if aluno['media_nota'] >= 7:
        aluno['situacao'] = 'Aprovado'
    elif aluno['media_nota'] >= 5:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'Reprovado'
    lista_de_alunos.append(aluno.copy())

    resposta =  str(input("Quer adicionar outro aluno? [s/n]")).lower().strip()
    if resposta not in 'SIMsim':
        break

print(lista_de_alunos)
for item in lista_de_alunos:
    print(f'Média é igual a {item['media_nota']}')
    print(f'Situação é igual a {item['situacao']}')
