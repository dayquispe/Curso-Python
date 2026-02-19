# Escrava um programa para aprovar o empréstimo bancário
# para a compra de uma casa. 0 programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai
# pagar.
# Calcula o valor da prestação mensal, sabendo que ala nao
# pode excader 30% do salário ou antao o empréstimo será
# nagado.

valor_casa = float(input("Insira o valor da casa: "))
salario_comprador = float(input("Insira o valor do seu salário: "))
anos_pagar = int(input("Em quantos anos você quer pagar? "))

prestacao_mensal = (anos_pagar * 12) / salario_comprador

if prestacao_mensal > (0.3 * salario_comprador):
    print(f"Empréstimo NEGADO!\n"
          f" A prestação excede 30% do seu salário!\n"
          f"Salario: R${salario_comprador:.2f}\n"
          f"Prestação mensal: R${prestacao_mensal:.2f}")

else:
    print(f"Empréstimo Concedido! \n"
          f" A prestação é menor que 30% do seu salário!\n"
          f"Salario: R${salario_comprador:.2f}\n"
          f"Prestação mensal: R${prestacao_mensal:.2f}")