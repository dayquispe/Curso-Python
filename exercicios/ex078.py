# Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor
# digitado e as suas respectivas posições na lista.

lista_de_numeros = []
for i in range(0, 6):
    lista_de_numeros.append(int(input(f"Digite um valor para a Posiçõa {i}: ")))

print(f"Valores digitados: {lista_de_numeros}")
maior = max(lista_de_numeros)
menor = min(lista_de_numeros)

palavra_posicao_numero_maior = " nas posições: " if lista_de_numeros.count(maior) > 1  else "na posição: "
palavra_posicao_numero_menor = " nas posições: " if lista_de_numeros.count(menor) > 1  else "na posição: "

print(f"\nO maior valor digitado foi {maior} {palavra_posicao_numero_maior} ", end=" ")
for indice, numero in enumerate(lista_de_numeros):
    if numero == maior:
        print(f"{indice}", end=" ")

print(f"\nO menor valor digitado foi {menor}  {palavra_posicao_numero_menor} ", end=" ")
for indice, numero in enumerate(lista_de_numeros):
    if numero == menor:
        print(f"{indice}", end=" ")
