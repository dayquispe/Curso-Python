def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)

def soma(a, b):
    return print(a+b)

soma(2, 6)

def soma2(a, b):
    print(f"A = {a}, B = {b}")
    print(f"A soma entre A + B é {a+b}")

soma(2, 6)

soma2(5, 5)

def contador(* num): # * aí é o símbolo de desempacotar
    for i in num:
        print(f"{i} ", end="")
    print(f"fim")

contador(2, 7)
contador(6, 3, 5, 4)
contador(6, 8, 2)

def contador2(* num): # * aí é o símbolo de desempacotar
    tam = len(num)
    print(f"recebi os valores {num} e são ao todo {tam} números.")

contador2(2, 7)
contador2(6, 3, 5, 4)
contador2(6, 8, 2)

def dobra_valores(lst):
    pos = 0
    while pos < len(valores):
        valores[pos]*=2
        pos+=1

valores = [5, 3, 2, 4, 0, 2]


dobra_valores(valores)
print(valores)

def soma3(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma3(5, 2)
soma3(6, 8, 9, 0)