from rich import print
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"[yellow]{numero} X {i} = {numero * i}[/]")
