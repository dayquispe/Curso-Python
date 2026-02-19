# Faça um progarma que leia um ângulo qualquer e mostre na
# tela o valor do seno, coseeno e tangente desse ângulo.
import math

angulo = int(input("Digite um ângulo: "))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"O ângulo dado foi {angulo}°\n"
      f"Seu seno é {seno}\n"
      f"O cosseno é {cosseno}\n"
      f"A tangente é {tangente}")