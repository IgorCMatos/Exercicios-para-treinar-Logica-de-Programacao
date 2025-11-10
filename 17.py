#17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas. Fórmula: C = (5 * ( F-32) / 9)

F = float(input("Digite a temperatura em Fahrenheit: "))

C = (5 * (F - 32)) / 9

print(f"\nTemperatura em Fahrenheit: {F:.2f}°F")
print(f"Temperatura correspondente em Celsius: {C:.2f}°C")

