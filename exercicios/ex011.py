largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura em metros: "))

area = largura * altura
um_litro = 2
total_litros = area/um_litro
print(f"Para pintar uma parede de {area}m² serão necessário {total_litros} litros de tinta.")