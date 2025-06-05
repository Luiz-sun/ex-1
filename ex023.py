fras = str(input('Digite uma frase; ')).strip()
print(f'A letra D aparece {fras.upper().count('D')}')
print(f'A primeira letra D aparece na posição {fras.upper().find('D')+1}')
print(f"A ultima vez que aparece a letra D é {fras.upper().rfind('D')+1}")