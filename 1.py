#1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

valor_a = float(input("Digite o valor de A: "))
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))

soma_ab = valor_a + valor_b

if soma_ab > valor_c:
    print(f"A soma de A e B é {soma_ab}, sendo maior que C ({valor_c}).")
elif soma_ab < valor_c:
    print(f"A soma de A e B é {soma_ab}, sendo menor que C ({valor_c}).")
else:
    print(f"A soma de A e B é {soma_ab}, sendo igual a C ({valor_c}).")
