# Mostra quantos dólares pode comprar
# Considerando: US$1,00 = R$3,27
from rich import print

reais = float(input("Quantos você tem  na carteira: "))

dolares = reais / 3.27

print(f"Você têm R${reais:.2f}, você pode comprar US${dolares:.2f} :dollar:.")