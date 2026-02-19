# Manipulando cadeias de texto.
def linhas():
    print(f"-" * 30)
frase = "Curso em vídeo Python"
# Fatiamento
print(frase[9])
print(frase[10])
print(frase[11])
print(frase[9:13]) # pega da posição 9 até a posição12, ele não pega posição 13.
print(frase[9:21])
print(frase[9:21:2]) # Começa no 9 e para no 21 e pula de 2 em 2.
print(frase[:5]) # Omitindo o inicio, ele começa do inicio, da posição 0
print(frase[5:]) # Omitindo o final, ele começa de um número e vai até o final.
print(frase[9::3]) # Omitindo o final, ele começa de um número e vai até o final pulando de 3 em 3.

# Análise
print("Análise")
print(len(frase)) # Conta quantos caracteres tem a frase
print(frase.count("o")) # Conta quantas vezes aparecea letra o minúscula.
print(frase.count("o", 0, 13)) # Conta quantas vezes aparecea letra o minúscula e já com fatiamento.

print("frase.find('deo')")
print(frase.find("deo")) # Vai me dizer quantas vezes ele encontrou 'deo', mas me mostrando em que posição começa o 'deo'.

print("frase.find('Android')")
print(frase.find("Android")) # Quando queremos encontrar algum caractere que não existe na frase, ele mostra -1.

print("'Curso' in frase")
print('Curso' in frase) # Isto não é uma funcionalidade, é um operador.

# Transformação
# Funcionalidades de transformação.
# por regra uma lista de strings ela é imutável, não podemos mexer nele.
# Mas podemos mudar ela através dos métodos

linhas()
print("frase.replace('Python', 'Android')")
frase.replace('Python', 'Android')
print(frase)
print(frase.replace('Python', 'Android'))
linhas()

print("frase.upper()")
print(frase.upper())
linhas()

print("frase.lower()")
print(frase.lower())
linhas()

print("frase.capitalize()")
print(frase.capitalize()) # Deixa tudo minusculo, e apenas a primeira letra da frase em maiúsculo.
linhas()

print("frase.title()")
print(frase.title()) # Deixa as palavras todas com a primeiras letra maiúscula.
linhas()

frase_nova = "   Aprenda Python  "

print(frase_nova)
print("frase.strip()")
print(frase_nova.strip()) # Remove todos os espaços inúteis do inicio e do final da string .
linhas()

frase_nova2 = "   Aprenda Python  "
print(frase_nova2)
print("frase.rstrip()")
print(frase_nova2.rstrip()) # Remove todos os espaços inúteis do lado direito da string .
linhas()

frase_nova3 = "   Aprenda Python  "
print(frase_nova3)
print("frase.lstrip()")
print(frase_nova3.lstrip()) # Remove todos os espaços inúteis do lado esquerdo da string .
linhas()

# Divisão
frase2 = "Curso em vídeo Python"
print("frase2.split()")
frase2.split()
print(frase2)
print(frase2.split())

# Junção
frase3 = "Curso em vídeo Python"
# Temos o '-'.join(frase) que vai juntar caracteres uma na outra.
print("'-'.join(frase3)") # junta uma string com '-' como separador.

# Para escrever um texto mais grande

print("""
    Cinco versos, ou uma quintilha (ou quinteto, 
    pentástico, cinquain), é uma estrofe poética 
    que agrupa cinco linhas ou versos em um conjunto
    rítmico e melódico, transmitindo ideias, emoções
    e imagens de forma concisa, com regras específicas
    de rima e métrica, dependendo do estilo, como em
    poemas populares ou cultos
""")
linhas()
frase4= "Curso em Vídeo Python"
print(frase4.upper().count('O'))
linhas()

# Para salvar o resultado de uam string modificada:
frase5 = "Curso em Vídeo Python"
frase5 = frase5.replace("Python", "Android") # Aqui temos uma atriibuição.
print(frase5)
linhas()

frase6 = "Curso em Vídeo Python"
print(frase6.lower().find("vídeo")) # Mostra a pocisão de inicio da string Vídeo.

linhas()
frase6 = "Curso em Vídeo Python"
print(frase6.split())

linhas()
frase7 = "Curso em Vídeo Python"
dividido = frase7.split()
print(dividido)
print(dividido[0])

linhas()
print(dividido[2][3]) #  Pegue o dividio 2 que é o 'vídeo', e me mostre a letra 3.







