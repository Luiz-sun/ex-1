from  random import randint
print("O computador vai escolher um numero aleatorio e você  tentara "
      "adivinhar o numero, se acerta ele \n retornaa'Acertou' e se errou "
      "retornara'Errou' ")
print('Os numero é de 1 a 5')
nu_alea = randint(0,5)
nu = int(input('Escreva o número que você acha que é;  '))
if nu >= 1 and nu <= 5:
    if nu == nu_alea:
        print('Você ganhou')
    else:
        print('Você errou, pensei no numero' + nu_alea)
else:
    print("Digite o valor de 1 a 5")