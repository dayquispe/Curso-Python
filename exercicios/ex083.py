# Crie um programa onde o usuário digite uma
# expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a
# expressão passada está com os parênteses
# abertos e fechados na ordem correta.

expressao = input("Digite a expresão: ")

pilha_parenteses = []

for parenteses in expressao:
    if parenteses == "(":
        pilha_parenteses.append(parenteses)
    elif parenteses == ")":
        if len(pilha_parenteses) > 0:
            pilha_parenteses.pop()
        else:
            pilha_parenteses.append(parenteses)
            break

if len(pilha_parenteses) == 0:
    print("Sua expressáo é válida")
else:
    print("Sua expressão não é válida")