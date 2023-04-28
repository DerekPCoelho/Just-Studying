from random import randint
from time import sleep
lista = list()
jogos = list()
print('\n','-' * 30)
print('\n       JOGA NA MEGACENA      ')
print('\n','-' * 30)
quantidade = int(input('\nQuantos jogos devo sortear?'))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('\n','-=' * 3, f' SORTEANDO {quantidade} jogos ', '-=' *3)
for i, l in enumerate(jogos):
    print('\n',f'jogo {i+1}: {l}')
    sleep(1)
print('\n','-=' * 5, '<BOA SORTE!>', '-=' * 5)
        