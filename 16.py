# 16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é equilátero, isósceles ou escaleno.

a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("\nOs lados formam um triângulo.")
    
    if a == b == c:
        print("Tipo: Equilátero (três lados iguais).")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles (dois lados iguais).")
    else:
        print("Tipo: Escaleno (todos os lados diferentes).")
else:
    print("\nOs valores informados não formam um triângulo válido.")

