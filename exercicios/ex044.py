# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# -> à vista dinheiro/cheque: 10% de desconto
# -> à vista no cartão: 5% de desconto
# -> em até 2x no cartão: preço normal
# -> 3x ou mais no cartão: 20% de juros

valor = float(input("Insira o valor do produto: "))
escolha = int(input("Escolha a forma de pagamento: \n"
                    "[1] vista dinheiro/cheque: 10% de desconto\n"
                    "[2] à vista no cartão: 5% de desconto\n"
                    "[3] em até 2x no cartão: preço normal\n"
                    "[4] 3x ou mais no cartão: 20% de juros\n"
                    "==> "))
if escolha == 1:
    valor_novo = valor - (0.1 * valor)
elif escolha == 2:
    valor_novo = valor - (0.05 * valor)
elif escolha == 3:
    valor_novo = valor
else:
    valor_novo = valor + (0.2 * valor)

print(f"O valor do produto é R${valor_novo:.2f}")
