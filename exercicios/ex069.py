#  Crie um programa que leia a idade e o sexo
#  de várias pessoas. A cada pessoa cadastrada,
#  o programa deverá perguntar se o usuário quer
#  ou não continuar. No final, mostra:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

quantidade_pessoas_mais18_anos = 0
quantidade_homem = 0
quantidade_mulheres_menos20_anos = 0

while True:
    print("-"*15)
    print("CADASTRE UMA PESSOA")
    print("-"*15)


    idade = int(input("Idade: "))
    sexo = ""
    while True:
        sexo = input("Sexo: [M/F] ").upper()
        if sexo not in "MF":
            pass
        else:
            break

    if sexo == "M":
        quantidade_homem += 1
    if sexo == "F" and idade < 20:
        quantidade_mulheres_menos20_anos += 1
    if idade > 18:
        quantidade_pessoas_mais18_anos += 1

    resposta = input("Quer continuar? [S/N] ").upper().strip()
    if resposta == "N":
        break

print("========== FIM DO PROGRAMA ===========")
print(f"Total de pessoas com mais de 18 anos: {quantidade_pessoas_mais18_anos}")
print(f"Ao todo temos {quantidade_homem} homens cadastrados")
print(f"E temos {quantidade_mulheres_menos20_anos} mulheres com menos de 20 anos")