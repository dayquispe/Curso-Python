# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "Santo".
from traceback import print_tb

nome_cidade = input("Digite o nome de uma cidade: ")
primeiro_nome_cidade = nome_cidade.split()[0].lower().strip()
print('santo' in primeiro_nome_cidade)


# Resolução

cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper() == "SANTO")