"""
Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento

 pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
 Tabela de Código de Condições de Pagamento
 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

 2 - À Vista no cartão de crédito, recebe 10% de desconto

 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%


"""

valor = float(input("Digite o valor do produto: "))

print("\nFormas de pagamento:")
print("1 - À vista em dinheiro ou Pix (15% de desconto)")
print("2 - À vista no cartão de crédito (10% de desconto)")
print("3 - Parcelado em 2x no cartão (sem juros)")
print("4 - Parcelado em 3x ou mais no cartão (10% de juros)")

opcao = int(input("\nDigite o código da forma de pagamento: "))

if opcao == 1:
    valor_final = valor * 0.85
elif opcao == 2:
    valor_final = valor * 0.90
elif opcao == 3:
    valor_final = valor
elif opcao == 4:
    valor_final = valor * 1.10
else:
    print("Opção inválida.")
    valor_final = None

if valor_final is not None:
    print(f"\nValor final a ser pago: R$ {valor_final:.2f}")
