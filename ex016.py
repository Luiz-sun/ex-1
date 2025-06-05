import math

ang = int(input('Digite o angulo; '))
rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(f'O angulo é esse; {ang:.2f} \nO seno dele é {seno:.2f}, \n O casseno é {cosseno:.2f} \n  e seu tanene é {tangente:.2f}')