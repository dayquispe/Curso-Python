#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input("Digite uma frase: ").lower().strip()

frase_invertida = "".join(reversed(frase))

if frase_invertida == frase:
    print(f"A frase {frase} é um palíndromo\n"
          f"frase: {frase}\n"
          f"frase invertida: {frase_invertida}")
else:
    print(f"A frase {frase} não é um palíndromo")