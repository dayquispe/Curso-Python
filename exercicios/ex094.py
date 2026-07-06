# Crie um programa que leia nome, sexo, e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média da idade do grupo.
# C) Ums lista de todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média.

lista_dicionarios = list()
dicionario = dict()

soma_total_idades = 0

while True:
    dicionario['nome'] = input("Nome: ").strip()
    while True:
        dicionario['sexo'] = input("Sexo: [M/F] ").upper().strip()
        if dicionario['sexo'] in 'MF':
            break
        print(f"ERRO! Por favor, digite apenas M ou F.")

    dicionario['idade'] = int(input("Idade: "))

    soma_total_idades += dicionario['idade']

    lista_dicionarios.append(dicionario.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N]")).upper()[0]
        if resposta in 'NS':
            break
        print("ERRO! responda apenas S ou N")
    if resposta == 'N':
        break

qtd_pessoa = len(lista_dicionarios)
media_idade = soma_total_idades/qtd_pessoa

print(f"-- O grupo têm {qtd_pessoa} pessoas.")
print(f"-- A média de idade é de {media_idade:5.2f} anos")

print(f"-- As mulheres cadastradas foram ", end='')
for pessoa in lista_dicionarios:
    if pessoa['sexo'] in 'Ff':
        print(f"{pessoa['nome']} ", end="")

print()

print(f"-- Lista de pessoas que estão acima da média: ")
for pessoa in lista_dicionarios:
    if pessoa['idade'] > media_idade:
        print("    ", end='')
        for k, v in pessoa.items():
            print(f"{k} = {v}", end="")
        print()
print("<< ENCERRADO >>")
