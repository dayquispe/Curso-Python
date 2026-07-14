# Crie um programa que tenah a função leia_int(), que vai
# funcionar de forma semelhante à função input() do Python, só que
# fazendo a validação para aceitar apenas um valor númerico.

#Ex: n=leiaInt("Digite um n")

def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n =  str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"\033[0;31mErro: Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor
numero = leia_int("Digite um número: ")
print(f"Você digitou o número {numero}")