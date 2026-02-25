# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maioridade = 0
nao_maioridade = 0
ano_atual = 2026
for i in range(1, 8):
    ano_nascimento = int(input("Digite o ano e nascimento da pessoa: "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        nao_maioridade += 1
print(f"O total de pessoas que atingiram a maioridade é : {maioridade}\n"
      f"O total de pessoa que não atingiram a maioridade é {nao_maioridade}")
