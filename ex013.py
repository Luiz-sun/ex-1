#-------------------------------#
#Variaveis alug, valordia, valorkm e valortotal#
print('Bom dia ou Boa tarde!!! Aluguel de carro um dia é R$60,00 e paga R$0,15 po Km, iremos calcular o valor')
alug = int(input('Digite quantos dias ficou com o carro;  '))
km = float(input('Digita quantos Km rodados;  '))
valordia = alug*60.00
valorkm = km*0.15
valortotal = valordia + valorkm
print(f"O valor em dias foi; R$ {valordia:.2f} e o valor em km foi; R$ {valorkm:.2f} \n O valor total a pagar; R$ {valortotal:.2f}")
