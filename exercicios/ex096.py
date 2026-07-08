# Faça um programa que tenha uma função chamada área(), que recebe as
# dimensões de um triângulo retangular (largura e comprimento) e mostre
# a área do terreno.

def titulo(legenda):
    print(legenda)
    print("-"*20)

def area_retangular(largura, comprimento):
    area = largura*comprimento
    return print(f"A área de um terreno {largura} e {comprimento} é de {area}m².")

titulo("Controle de terrenos")
largura_recebida = float(input("LARGURA (m): "))
comprimento_recebido = float(input("COMPRIMENTO (m): "))
area_retangular(largura_recebida, comprimento_recebido)
