#24 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

distancia = tempo * velocidade_media

litros_usados = distancia / 12

print(f"\nTempo de viagem: {tempo:.2f} horas")
print(f"Velocidade média: {velocidade_media:.2f} km/h")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível gasto: {litros_usados:.2f} litros")
