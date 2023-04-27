km = int(input('Digite a distancia da viagem'))
taxa1 = 10
taxa2 = 5

if km > 200:
    valor = km * taxa2
else:
    valor = km * taxa1
    
print('Valor a pagar = R$ {}'.format(valor))