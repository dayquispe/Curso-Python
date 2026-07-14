# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def linha():
    print("-"*20)

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade > 18:
        return  f"Com {idade} anos : VOTO OBRIGATÓRIO."
    elif idade > 70 or 16 <= idade <18:
        return f"Com {idade} anos : VOTO OPCIONAL."
    else:
        return f"Com {idade} anos : NÃO VOTA"

linha()
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
