# Crie um programa que tenha a função fatorial() que recebe
# dois parâmetros: o primeiro que indique o número a calcular
# e o outro chamado show, (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

def fatorial(n=0, show=False):
    """
    --> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
        if show:
            print(f"{i} ", end="")
            if i != 1:
                print("x ", end="")
            else:
                return f"= {fat}"
    return fat

print(fatorial(5, show= True))

help(fatorial)