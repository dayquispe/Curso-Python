# Crie um programa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem no final, de acordo com a média
# atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre de 5.0 e 6.9: RECUPERAÇÃO
# - Média 7 ou superior: APROVADO

from  rich import print

nota1 = float(input("Digite primeira nota: "))
nota2 = float(input("Digite segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"A media do aluno foi {media}, [green bold]APROVADO[/].")
elif 5 <= media <= 6.9:
    print(f"A média do aluno foi {media}, [blue bold]RECUPERAÇÃO[/].")
else:
    print(f"A média do aluno foi {media}, [red bold]REPROVADO[/]")
