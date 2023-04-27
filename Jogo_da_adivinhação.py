from random import randint

n = int(input('Tente adivinhar o numero que estou pensando de zero a dez...'))
numero_sorteado = randint(0, 10)
if n == numero_sorteado:
    print('Você acertou!! o numero que eu pensei é o {}'.format(numero_sorteado))
else:
    print('Mais sorte na proxima vez! o numero era {}'.format(numero_sorteado)) 