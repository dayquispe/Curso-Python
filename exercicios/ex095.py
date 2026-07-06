# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, qtd_partidas):
        partidas.append(int(input(f"     Quantos gols na partida {c+1}?")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = input("Quer continuar? [S/N] ").upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Responda apenas S ou N.")

    if resposta in 'N':
        break

print("-=" * 30)
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-=" * 30)

print("-=" * 30)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-=" * 30)

while True:
    busca = int(input("Mostrar dados de qual jogador? "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No jogo {i} fez {g} gols.")
    print("-" * 30)
print("Volte sempre")
