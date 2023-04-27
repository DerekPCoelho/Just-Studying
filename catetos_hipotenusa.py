#co = float(input('cateto oposto:'))
#ca = float(input('cateto adjacente'))
#h = (co ** 2 + ca ** 2) ** (1/2)
#print('hipotenusa = {}'.format(h))

import math
co = float(input('cateto oposto:'))
ca = float(input('cateto adjacente'))
h = math.hypot(co, ca)
print('hipotenusa = {}'.format(h))