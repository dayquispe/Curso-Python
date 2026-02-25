# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}° pessoa: "))
    if peso > maior_peso:
        maior_peso = peso

    if i == 1:
        menor_peso = maior_peso

    else:
        if peso < menor_peso:
            menor_peso = peso

print(f"O menor peso foi: {menor_peso}\n"
      f"O maior peso foi: {maior_peso}")

