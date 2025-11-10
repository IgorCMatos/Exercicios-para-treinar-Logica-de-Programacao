# 8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

numeros = [a, b, c]
numeros.sort(reverse=True)

print("Os valores em ordem decrescente são:", numeros)
