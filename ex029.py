print("O programa calulara se é ano bissexto ou não")
ano = int(input('Digite um ano;  '))
if  ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('Ano não bissexto')