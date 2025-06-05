'''import math

cateoposto = float(input('Digite o comprimento do cateto oposto;  '))
cateadjacente = float(input('Digite o comprimento do cateto adjacente;  '))
mult = cateoposto**2 + cateadjacente**2
hipo = math.sqrt(mult)
print(f'Valor do cateto opostos {cateoposto} valor do cateto adjacente {cateadjacente} \n O valor da hipotenusa é; {hipo :.2f}')'''
import math

co = float(input('Digite o comprimento do cateto oposto '))
ca = float(input('Digite o comprimento do cateto adjacente;  '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')