# 22 - Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if B == 0:
    print("Erro: divisão por zero não é permitida.")
else:
    quociente = A // B
    resto = A % B

    print(f"\nQuociente: {quociente}")
    print(f"Resto: {resto}")

