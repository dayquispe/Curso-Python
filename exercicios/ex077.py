#Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('programacao', 'python', 'computador', 'estudar', 'teclado',
            'mouse', 'monitor', 'internet', 'desafio', 'sucesso')

vogais = "aeiou"

for palavra in palavras:
    print(f"\n Na palavra {palavra.upper()} temos as vogais:", end="")
    for vogal in palavra:
        if vogal in vogais:
            print(f"{vogal.lower()}", end=" ")

