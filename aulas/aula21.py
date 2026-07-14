#help(print)

print(len.__doc__)

# DOCSTRING

def contador(i, f, p):
    """
    -> Faz uma contagem e motra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """

    cont = i
    while cont <= f:
        print(f"{cont} ", end='')
        cont += p
    print("FIM!")
contador(2, 10, 2)

def somar(a=0, b=0, c=0):
    """
    --> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """

    s = a + b + c
    print(f'A soma deles {s}', end="\n")

somar(b=4, c=2)
somar(c=3)

# ESCOPO LOCAL E GLOBAL

def funcao():
    n1 = 4
    print(f"N1 dentro vale {n1}")

n1 = 2
funcao()
print(f"N1 fora vale {n1}")

print()

def teste(b):
    global  a
    a = 8
    b+=4
    c = 2
    print(f"A dentro vale ({a})")
    print(f"B dentro vale ({b})")
    print(f"C dentro vale ({c})")

a = 5

print(f"A fora vale {a}")
teste(a)
print(f"A fora vale {a}")

# RETORNO DE VALORES

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(2, 4, )
print(r1)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é agual a {fatorial(n)}")


def par(n=0):
    if n%2==0:
        return True
    else:
        return False

num = int(input("Digite um número: "))
if par(num):
    print("É par!")
else:
    print("Não é par!")
