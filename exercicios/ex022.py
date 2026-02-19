# Crie um programa que leia o nome completo de uma essoas e mostre:
# -> O nome com todas as letras minúsculas.
# -> Quantas letras ao todo (sem considerar os espaços).
# -> Quantas letras tem o primeiro nome.
from rich import print
nome_completo = input("Digite seu nome completo: ")

nome_separado = nome_completo.split()
nome_junto = "".join(nome_separado)

qtd_primeiro_nome = nome_separado[1]
print(f"[bold magenta]O nome com letras minúsculas: {nome_completo.lower()}[/]\n"
      f"[yellow]O nome tem {len(nome_junto)} letras sem contar os epaços.[/]\n"
      f"[blue]O primeiro nome tem {len(qtd_primeiro_nome)} letras[/]")

