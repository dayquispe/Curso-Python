#import math
# from match import sqrt  # mais especifico
# from match import sqrt, ceil  # mais especifico
# math
# Do tach podemos importar as funcionalidades:
# ceil: arredondamento para cinma
# floor : arredondamento para baixo
# trunc: vai truncar o número, vai eleminar o némero da vírgula para frente.
# pow: para potência
# sqrt: para calculara a raiz quadrada
# factorial: para calcular o factorial.

import  math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raíz de {num} é {raiz}")

num2 = int(input("Digite um número: "))
raiz = math.sqrt(num2)
print(f"A raíz de {num2} é {math.ceil(raiz)} <-- Arredondado para cima.")


num3 = int(input("Digite um número: "))
raiz = math.sqrt(num2)
print(f"A raíz de {num2} é {math.floor(raiz)} <-- Arredondado para baixo.")
