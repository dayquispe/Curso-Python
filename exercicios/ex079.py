# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente

lista_de_numeros = []

while True:
    numero = (int(input("Digite um valor: ")))
    if numero not in lista_de_numeros:
        lista_de_numeros.append(numero)
    else:
        print("Valor duplicado! Não vou adicionar...")
    resposta = input("Quer continuar? [S/N] ").lower()
    if resposta == "n":
        break
lista_de_numeros.sort()
print(f"Você digitou os valores: {lista_de_numeros}")
