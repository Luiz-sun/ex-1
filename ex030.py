#print('O programa retornara dois numeros se é maior ou menor')
#n1 = int(input('Escreva o primeiro número; '))
#n2 = int(input('Escreva o segundo número; '))
#n3 =int(input('Escreva o terceiro número; '))
#f n1 < n2 and n1<n3:
    #print(f'O menor é {n1}')
#elif n2<n3 and n2<n1:
    #print(f'O menor é {n2}')
#else:
    #print(f'O menor é {n3}')
#if n1 > n2 and n1 > n3:
    #print(f'O maior numero é {n1}')
#elif n2 > n1 and n2 > n3:
    #print(f'O maior numero é {n2}')
#else: print(f'O maior numero é {n3}')
print('O programa retornara dois numeros se é maior ou menor')
n1 = int(input('Escreva o primeiro número; '))
n2 = int(input('Escreva o segundo número; '))
n3 = int(input('Escreva o TERCEIRO número; '))
maior =max(n1,n2,n3)
menor =min(n1,n2,n3)
print(f'O maior número é {maior} e o menor é {menor}')