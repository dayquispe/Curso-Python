# Condições:

# Condição simplificada
tempo = int(input("Quantos anos tem seu carro? "))
# Como um operador ternario.
print("carro novo" if tempo <= 3 else "carro velho")
print("--Fim--")

def pontilhado():
    print("_" * 20)

nome = input("Digite seu nome: ").lower()
if nome == "dayana":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal")
print(f"Bom dia, {nome}!")

pontilhado()
n1 = int(input("Digite primeira nota: "))
n2 = int(input("Digite segunda nota: "))
m = (n1 + n2)/2
print(f"A sua média foi {m}")
print(f"Parabéns" if m >= 6 else "ESTUDE MAIS")