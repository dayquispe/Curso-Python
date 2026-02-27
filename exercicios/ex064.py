# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input("Digite um numero qualquer. Digite 999 se quiser parar: "))
cont = 1
monte = numero
while numero != 999:
    numero = int(input("Digite outro: "))
    if numero != 999:
        cont += 1
        monte += numero

print(f"Forma digitados {cont} números. \n"
      f"A soma total desses números é {monte}")