# Escrava um programa qua pergunte a quantidada de Km
# percorridos por um carro alugado e a quantidade de dias palos
# quais ala foi alugado. Calcule o praço a pagar, sabendo qua o carro
# custa R$60 por dia a R$0.15 por Km rodado.

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago = (dias * 60) + (km * 0.15)
print(f"O total a pagar é de R${pago:.2f}")