# faça um programa que leia uma frase pelo teclado e moçstre:

# -> Quantas vezes aparece a letra 'A'.
# -> Em que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a última vez.
from rich import print
frase = input("Digite uma frase qualquer: ").upper().strip()
qtd_a = frase.count("A")
primeira_vez  = frase.find("A")+1
ultima_vez = frase.rfind("A")+1

print(f"[blue bold]Na frase {frase}[/]\n"
      f"[green]Aparecem {qtd_a} vezes a letra 'A';\n"
      f"A primeira aparece na posição {primeira_vez};\n"
      f"O último 'A' aparece na posição {ultima_vez};[/]")