# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense',
         'Athletico-PR', 'Red Bull Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol',
         'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'Vitória',
         'Remo', 'Atlético-MG', 'Internacional', 'Cruzeiro', 'Vasco')
print(f"5 primeiros colocados: {times[:5]}")
print(f"Os últimos 4 colocados da tabela: {times[-4:]}")
print(f"Uma lista com os times em ordem alfabética: {list(sorted(times))}")
for i, n in enumerate(times):
    if n == "Chapecoense":
        posicao = i+1

print(f"O Chapecoense está na {posicao}° posição")