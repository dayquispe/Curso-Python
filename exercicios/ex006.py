from rich import print

numero = float(input("Digite qualquer número: "))
print(f"[yellow]O dobro de {numero} é {numero*2}[/]\n"
      f"[black]O triplo de {numero} é {numero*3}[/]\n"
      f"[cyan]A raiz quadrada de {numero} é {numero**(1/2)}[/]")
