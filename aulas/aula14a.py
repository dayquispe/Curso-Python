#c = 0
#while c < 10:
    #print(c)
    #c+=1

# """""""""""""""""""""""""""""""""""
# n = 1
#while n != 0:
    #n = int(input("Digite um valor: "))
    #print(n)
# """""""""""""""""""""""""""""""""""

# resposta = "s"

#while resposta =="s":
  #  inr = int(input("Digite um número: "))
   # resposta = str(input("Quer continuar? [s/n]: ")).lower()
#print("Finalizado")

# """""""""""""""""""""""""""""""""""
numero = 1
impar = par = 0
while numero!=0:
    numero = int(input("Digite um valor: "))
    if numero != 0:
        if numero % 2 == 0:
            par +=1
        else:
            impar += 1

print(f"Você digitou {par} números pares e  {impar} números ímpares")