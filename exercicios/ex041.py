# A Confederação Nacional de Natação precisa de um programa que
# receba o ano de nascimento de um atleta e informe sua
# categoria de acordo com a idade:
#Até 9 anos → Mirim
#Até 14 anos → Infantil
# Até 19 anos → Júnior
# Até 20 anos → Sênior
# Acima de 20 anos → Master
from unicodedata import category

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
if idade <= 9:
    categoria = "MIRIM"
elif idade <=14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JÚNIOR"
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print(f"Você tem {idade} anos: categoria {categoria}")