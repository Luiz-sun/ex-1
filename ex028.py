print('O rpograma ira calcular a o custo da passagem calcularndo em km \n '
      'te 200km sea cobrado R$0.50 para km mais altos seá 0.45')
km = float(input("Digite o km da viagem; "))
if km <= 200:
    valor_viagem = km * 0.50
    print(f'Esse será o valor da viagem R${valor_viagem:.2f}')
else:
    valor_viagem = km * 0.45
    print(f'Esse será o valor da viagem R${valor_viagem:.2f}')