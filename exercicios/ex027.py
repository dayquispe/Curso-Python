# faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último
#nome separadamente.
#EX: Ana Maria de Souza
#primeiro: Ana
#último: Souza
from shlex import split

from rich import print


nome_completo = input("Digite seu nome completo: ").title().strip()

primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo.split()[-1]

print(f"Primeiro nome: {primeiro_nome}\n"
      f"ùltimo nome: {ultimo_nome}")
