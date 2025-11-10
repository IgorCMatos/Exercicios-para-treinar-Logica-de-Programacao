# 3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.

valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))

if valor_a == valor_b:
    valor_c = valor_a + valor_b
    print(f"Os valores de A e B são iguais, portanto o valor de C é a soma deles: {valor_c}")
else:
    valor_c = valor_a * valor_b
    print(f"Os valores de A e B são diferentes, portanto o valor de C é a multiplicação deles: {valor_c}")
