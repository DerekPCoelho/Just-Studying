v = int(input('Digite a velocidade '))
if v > 50:
    m = (v - 50) * 10.5
    print('você foi multado em R${:.2f}'.format(m))
else:
    print('você nao foi multado')