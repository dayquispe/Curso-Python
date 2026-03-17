# Variáveis Compostas (Tupla)

lanche = ("Hámburguer", "Suco", "Pizza", "Pudim")
print(lanche)
print(lanche[1])
print(lanche[1])

for i in lanche:
    print(f"Comi {i}")
print("Comi bastante")

print(len(lanche))
print(len("daa"))

for cont in range(0, len(lanche)):
    print(cont)

for cont in range(0, len(lanche)):
    print(lanche[cont])

for i in range(len(lanche)):
    print(f"Vou comer {lanche[i]} na posição {i}")

for indice, nome_lanche in enumerate(lanche):
    print(f"Vou comer {nome_lanche} na posição {indice}")

print(sorted(lanche)) # sorted mostra ordenado com sorted(), isso não quer dizer que ele muda a tupla.

a = (2, 4, 6)
b = (8, 4, 3, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))

print(c)
print(c.index(4)) # com index, perguntamos em que posição temos o número 2

pessoa = ("Julia", 45, "Feminino", 67.4)
print(pessoa)

# del(pessoa) # del() não funciona com tuplas
print(pessoa)