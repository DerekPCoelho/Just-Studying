from random import randint
resposta = str(input('Par ou ímpar??')).strip().upper()
nj = int(input('Digite um numero de um a dez: '))
nc = randint(0, 10)
calculo = nj + nc
resultado = calculo % 2
resposta_final = calculo
if resultado == 0:
    resposta_final = 'PAR'
else:
    resposta_final = 'IMPAR'

if resposta == resposta_final:
    print('Droga! voce venceu! escolhi o numero {} e o resultado foi {} parabens!'.format(nc, resposta_final))
else:
    print('voce perdeu! escolhi o numero {} e o resultado deu {}'.format(nc, resposta_final))