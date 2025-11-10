# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

valor = int(input("Número: "))

valor_sucessor = valor + 1
valor_antecessor = valor - 1

print(f"O antecessor de {valor} é {valor_antecessor} e o sucessor é {valor_sucessor}.")
