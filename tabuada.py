while True:
    n = int(input('Digite o numero que você quer ver a tabuada  '))
    if n < 0:
        break
    print('=' * 30)
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
 