from math import radians,sin,cos,tan
a = float(input('Digite o angulo: '))
seno = sin(radians(a))
print("Seno: {:.2f}".format(seno))
cosseno = cos(radians(a))
print("Cosseno: {:.2f}".format(cosseno))
tangente = tan(radians(a))
print("Tangente: {:.2f}".format(tangente))