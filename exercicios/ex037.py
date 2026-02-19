# Escreva um programa qua laia um número inteiro
# qualquer e peça para o usuário ascolher qual
# sará a base da conversão:

# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input("Digite um número qualquer: "))
numero_base_conversao = int(input("Escolha qual a base de conversão: \n"
                                  "[1] Binário\n"
                                  "[2] Octal\n"
                                  "[3] Hexadecimal\n"
                                  "qual? "))
if numero_base_conversao == 1:
    print(f"O número {numero} convertido para Binário é: {bin(numero)}")
elif numero_base_conversao == 2:
    print(f"O número {numero} convertido para Octal é: {oct(numero)}")
else:
    print(f"O número {numero} convertido para Hexadecimal é: {hex(numero)}")

