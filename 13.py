#  13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade: "))

print(f"\nNome: {nome}")

if idade >= 18:
    print("Situação: Maior de idade")
else:
    print("Situação: Menor de idade")
