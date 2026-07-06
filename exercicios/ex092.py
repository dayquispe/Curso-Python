# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente
# de ZERO, e dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastros = dict()

ano_atual = date.today().year
cadastros['nome'] = str(input("Nome: "))
ano_nascimento = int(input("Ano de Nascimento:" ))
cadastros['idade'] = ano_atual - ano_nascimento
cadastros['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastros['ctps'] == 0:
    pass
else:
    cadastros['contratacao'] = int(input("Ano de contratação: "))
    cadastros['salário'] = float(input("Salário: R$ "))
    cadastros['aposentadoria'] = cadastros['idade'] + (35 - (ano_atual - cadastros['contratacao']))

print(cadastros)
for k, v in cadastros.items():
    print(f"{k} tem o valor de {v}")
