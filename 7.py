# 7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

v1 = input("Digite o primeiro valor lógico (True/False): ").strip().capitalize()
v2 = input("Digite o segundo valor lógico (True/False): ").strip().capitalize()

v1 = True if v1 == "True" else False
v2 = True if v2 == "True" else False

if v1 and v2:
    print("Ambos são VERDADEIROS.")
elif not v1 and not v2:
    print("Ambos são FALSOS.")
else:
    print("Os valores são diferentes (um é VERDADEIRO e o outro é FALSO).")
