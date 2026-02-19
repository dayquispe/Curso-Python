# Faça um programa que leia o ano de nascimanto da um
# jovam e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Seja passou do tempo do alistamento.
# Seu programa também daverá mostrar o tampo que falta ou
# que passou do prazo.

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
falta_anos = idade - 18

if (ano_atual - ano_nascimento) < 18:
    print(f"Você ainda vai se alistar. Faltam {18 - idade} ano(s) para você se alistar.")
elif (ano_atual- ano_nascimento) > 18:
    print(f"Já passou da hora de você se alistar. Passaram {falta_anos} ano(s).")
else:
    print(f"Você tem {ano_atual - ano_nascimento}, está na hora de você se alistar!")