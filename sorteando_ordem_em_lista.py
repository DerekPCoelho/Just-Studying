from random import shuffle
n1 = str(input('primeiro: '))
n2 = str(input('segundp: '))
n3 = str(input('terceiro: '))
n4 = str(input('quarto: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('Ordem: {} '.format(lista))
