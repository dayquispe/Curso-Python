# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input(f"Digite um número: "))
numero_guardado = numero
fatorial  = numero
while numero > 1:
    if numero != 1:
        print(f"{numero} X ", end="")
    else:
        print(f"{numero} = ", end= "")
    numero -= 1
    fatorial = fatorial * numero

print(f"Fatorial de {numero_guardado} = {fatorial}")