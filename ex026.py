km = float(input('Escreva a velocida que você passou no radar; '))
if km > 80:
    menos = 80 - km
    multa = menos * 7.0
    print('Você foi multado')
    print(f'O valor que tem que pagar é {multa}')
else:
    print("Não tem multa")