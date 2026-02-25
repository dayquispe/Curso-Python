# 💡 Faça um programa que calcule a
# soma entre todos os números ímpares
# que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i%3 == 0:
        soma += i
        print(f"numero: {i}\nsoma até aqui: {soma}")

print(f"A soma dos npumeros que são ímpares e múltiplos de 3 de 1 á 500 é {soma}")