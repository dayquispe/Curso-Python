teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
print(galera)
print(teste[0])
print(teste)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)

galera2 = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera2.append(dados[:])
    dados.clear()

print(galera2)