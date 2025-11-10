# 18 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja maior que Sara.

francisco = 1.50
sara = 1.10

crescimento_francisco = 0.02
crescimento_sara = 0.03

anos = 0

while francisco <= sara:
    francisco += crescimento_francisco
    sara += crescimento_sara
    anos += 1

print(f"Serão necessários {anos} anos para que Francisco seja maior que Sara.")
print(f"Altura final de Francisco: {francisco:.2f} m")
print(f"Altura final de Sara: {sara:.2f} m")

