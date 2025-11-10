# 14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.

A = input("Digite o valor de A: ")
B = input("Digite o valor de B: ")


print(f"\nAntes da troca: A = {A}, B = {B}")

A, B = B, A

print(f"Depois da troca: A = {A}, B = {B}")

