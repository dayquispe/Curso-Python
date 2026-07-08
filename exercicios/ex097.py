# Faça um programa que tenha uma função chamada escreva(), que recebe
#um txto qualquer como parâmetro e mostre uma mensagem com tamanho
#adaptável.

def escreva(texto):
    print("-"*(len(texto)+4))
    print(f"  {texto}")
    print("-"*(len(texto)+4))

texto_inserido = input("Digite algo: ")

escreva(texto_inserido)
