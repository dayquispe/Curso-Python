# Faça um programa que tenha uma função chamada maior(),
# que recebe vários parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles
# é o maior.

def maior(*numeros):
    numero_maior = numeros[0]
    print(f"Analisando os valores passados...")
    for i in numeros:
        print(f"{i} ", end="")
        if i > numero_maior:
            numero_maior = i
    print(f"Foram informados {len(numeros)} valores ao todo.")
    print(f"O maior valor informado foi {numero_maior}")

maior(2, 5, 6, 7, 7)