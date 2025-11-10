#23 - Faça um algoritmo que efetue o cálculo do salário líquido de um professor. As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

valor_hora = float(input("Digite o valor da hora-aula (R$): "))
quantidade_aulas = int(input("Digite o número de aulas lecionadas no mês: "))
percentual_inss = float(input("Digite o percentual de desconto do INSS (%): "))

salario_bruto = valor_hora * quantidade_aulas

desconto = salario_bruto * (percentual_inss / 100)

salario_liquido = salario_bruto - desconto

print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do INSS: R$ {desconto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
