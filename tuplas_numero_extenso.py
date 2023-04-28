extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('digite um numero de zero a dez'))
    if  0 <= n <= 10:
        break
    print('tente novamente:',end = '')
print(f'voce digitou {extenso[n]}')
for i in range(0, 10):
    i += 1

