from random import randint
v = 0

print('\n')
print('-=' * 30)
print('          PAR OU ÍMPAR! Você consegue me vencer?')
print('-=' * 30)
print('\n\nEu começo! \nMeu número é [***]')

while True:
    jogador = int(input('\nAgora é a sua vez!   \nEscolha um número. '))
    computador = randint(0, 10)
    total = jogador + computador 
    tipo = ' '
    while tipo not in'PI':
        tipo = str(input(' \nPar ou Impar? [P/I] ')).strip().upper()[0]
    print(f'\nVocê escolheu {jogador} e eu {computador}. o total é {total} ', end = '')
    print('\nDeu Par !' if total % 2 == 0 else 'Deu Impar!')
    if tipo =='P':
        if total % 2 == 0:
            print('\nVocê me venceu!')
            v += 1
        else:
            print('\n HA HA HA ! Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\nVocê me venceu!')
            v += 1
        else:
            print('\n HA HA HA ! Você perdeu!')
            break
    print('\nNão aceito isso! Vamos de novo!')
print(f'\nGAME OVER! voce me venceu um total de {v} vezes!!\n' )
    