#quadrado do cateto adj +  quadrado do cateto oposto
import math
ca = float(input('digite o valor do cateto adjacente: '))
co = float(input('digite o cateto oposto: '))
#hp = (ca**2+co**2)**(1/2)
hp = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hp}')
