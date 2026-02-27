# Melhore o DESAFIO 061, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

primero_termo = int (input("Digite o primeiro termo: "))
razao = int(input("Digite a razao da PA: "))
monte = 0
cont = 10
termo = 1
while termo!= 0:
    while cont >= 1:
        print(f"{monte+razao}", end=" ")
        monte += razao
        cont -= 1

    resposta = input("\nVocê quer continuar? ").lower().strip()
    if resposta == 'sim':
        mais_termos = int(input("Quantos termos mais? "))
        cont = mais_termos
        termo = mais_termos

print("Programa encerrado")



