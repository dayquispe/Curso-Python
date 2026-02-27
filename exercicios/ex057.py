# Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
# até ter um valor correto.




sexo = str(input("Insira seu sexo [F/M]: ")).upper()

if sexo == "F" or sexo == "M":
    print(f"Seu sexo: {sexo}")
else:
    while sexo not in "MF":
        sexo = str(input("Digite seu sexo novamente, usando F ou M: ")).upper()
    print(f"Seu sexo: {sexo}")