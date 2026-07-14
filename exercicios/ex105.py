# Faça um programa que tenha uma função notas() que pode
# receber vária notas de alunos e vai retornar um dicionário
# com as seguintes informações:
from statistics import mean

# Quantidae de notas
# A maior nota
# A menor nota
# a média da turma
# a situação (opcional)

# Adicione também as docstrings da função.

def notas (*nota, sit=False):
    """
    --> Função para analisar notas e situação de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    menor_nota = min(nota)
    maior_nota = max(nota)
    media_nota = sum(nota)/len(nota)

    dicionario['menor_nota'] = menor_nota
    dicionario['maior_nota'] = maior_nota
    dicionario['media_nota'] = media_nota

    if sit:
        if dicionario['media_nota'] < 6:
            dicionario['situacao'] = 'REPROVADO'
        elif dicionario['media_nota'] < 7:
            dicionario['situacao'] = 'RAZOÁVEL'
        else:
            dicionario['situacao'] = 'APROVADA'

    return dicionario

resp = notas(5, 8, 9, 4.5, 8, sit=True)
print(resp)

help(notas)
