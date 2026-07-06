pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']

for k, v in pessoas.items():
    print(f"{k} = {v}")

pessoas['nome'] = 'Leandro'

for k, v in pessoas.items():
    print(f"{k} = {v}")

pessoas['peso'] = 98

for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1]['sigla'])


print('-=' * 12)

estado = dict()
brasil1 = list()

for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: "))
    estado['sigla'] = str(input("Sigla do estado: "))
    brasil1.append(estado.copy())

for e in brasil1:
    for v in e.values():
        print(v, end=' ')
    print()