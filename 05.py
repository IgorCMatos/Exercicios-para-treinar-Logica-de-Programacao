# 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_usuario = float(input("Digite o valor do seu salário: "))

quantidade = salario_usuario / salario_minimo

print(f"Você ganha {quantidade:.2f} salários mínimos.")



