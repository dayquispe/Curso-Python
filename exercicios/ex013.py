from rich import print
salario_funcionario = float(input("Insira o salário do funcionário: "))

novo_salario_funcionario = salario_funcionario + (salario_funcionario * 0.15)

print(f"O salário do funcionário de R${salario_funcionario:.2f}, terá um aumento de 15%. \n"
      f" Novo salário: :dollar: R${novo_salario_funcionario:.2f}.")