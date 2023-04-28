from random import randint
computador = randint(0, 100)
print('Consegue adivinhar em qual numero eu estou pensando?')
certo = False
palpites = 0
while not certo:
    jogador = int(input('tente a sorte! digite um numero de 0 a 100 '))
    palpites += 1
    if jogador == computador:
        certo = True
    else:
        if jogador < computador:
            print('um pouco mais...tente novamente!')
        elif jogador > computador:
            print('um pouco menos...tente novamente!')
print('parabens!!! você descobriu com um total de {} palpites!!!'.format(palpites))
