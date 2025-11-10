# 15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em  consideração o ano com 365 dias e o mês com 30 dias.

ano_nascimento = int(input("Digite o ano em que você nasceu: "))

ano_atual = 2025

anos = ano_atual - ano_nascimento
meses = anos * 12
dias = anos * 365

print(f"\nVocê viveu aproximadamente:")
print(f"{anos} anos, {meses} meses e {dias} dias.")
