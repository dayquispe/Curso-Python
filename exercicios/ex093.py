# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
#vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#será guardado em um dicionário, incluindo o total de gols feitos durante o
# campeonato.

dicionario = dict()

dicionario['nome'] = str(input("Nome do Jogador: "))
qtd_partidas = int(input(f"Quantas partidas {dicionario['nome']} jogou? "))
lista_gols = []
for i in range(0, qtd_partidas):
    qtd_gols = int(input(f"Quantos gols na partida {i}? "))
    lista_gols.append(qtd_gols)

dicionario['gols_partidas']  = lista_gols[:]
dicionario['total'] = sum(lista_gols)

print("-=" * 20)
print(dicionario)
print("-=" * 20)

for k, v in dicionario.items():
    print(f"O campo {k} tem o valor {v}.")

print("-=" * 20)

print(f"O jogador {dicionario['nome']} jogou {qtd_partidas} partidas.")
for i in range(0, len(dicionario['gols_partidas'])):
    print(f"   ==> Na partida {i}, fez {dicionario['gols_partidas'][i]} gols.")

print(f"Foi um total de de {sum(lista_gols)}")
