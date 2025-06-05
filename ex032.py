print('O programa mostrará se da para fazer um triangulo; ')
reta1 = int(input('Escreva o cm da 1° reta; '))
reta2 = int(input('Escreva o cm da 2° reta; '))
reta3 = int(input('Escreva o cm da 3° reta; '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print("Da para forma um triangulo. O triangulo será isósceles")
if reta1 == reta2 and reta2 == reta3:
    print("Da para forma um triangulo. O triangulo será equilátero")
elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
    print("Da para forma um triangulo. O triangulo será escaleno")
else: print('Não da para formar um triangulo')