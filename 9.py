# 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição
# Algoritmo: Cálculo do IMC (Índice de Massa Corporal)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Condição: Abaixo do peso")
elif imc < 25:
    print("Condição: Peso normal")
elif imc < 30:
    print("Condição: Sobrepeso")
elif imc < 35:
    print("Condição: Obesidade grau I")
elif imc < 40:
    print("Condição: Obesidade grau II")
else:
    print("Condição: Obesidade grau III (mórbida)")
