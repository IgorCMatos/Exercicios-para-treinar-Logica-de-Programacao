# 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

valor = int(input("Digite um número: "))

if valor % 2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar"

if valor < 0:
    negativo_positivo = "negativo"
else:
    negativo_positivo = "positivo"

print(f"O número {valor} é {par_impar} e {negativo_positivo}.")
