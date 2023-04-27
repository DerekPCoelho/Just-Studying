from random import choice
n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('terceiro: '))
n4 = str(input('Quarto: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('{}'.format(escolhido))