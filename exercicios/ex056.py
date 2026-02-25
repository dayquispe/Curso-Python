# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.
total_soma_idade = 0
nome_homem_mais_velho = ""
qtd_mulheres_menos_20_anos = 0

idade_homem = 0
idade_mulher = 0
for i in range(1, 5):
    nome = input(f"Digite o nome da {i}° pessoa: ")
    idade = int(input("Digite a idade dessa pessoa: "))
    sexo = input("Agora o sexo F ou M: ").lower().strip()

    total_soma_idade += idade
    #Homem mais velho
    if sexo == "m":
        if idade > idade_homem:
            idade_homem = idade
            nome_homem_mais_velho = nome


        if idade > idade_homem:
            idade_homem = idade
            nome_homem_mais_velho = nome

    # Mulher comm menos de 20 anos
    if sexo == "f" and idade < 20:
        qtd_mulheres_menos_20_anos +=1

media = total_soma_idade / 4

print(f"A média de idade do grupo: {media}\n"
      f"Qual é o nome do homem mais velho: {nome_homem_mais_velho}\n"
      f"Quantas mulheres têm menos de 20 anos: {qtd_mulheres_menos_20_anos}")



