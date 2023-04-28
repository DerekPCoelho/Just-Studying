lista = ('lapis', 1.59,
         'borracha', 0.36,
         'caderno', 19.99,
         'estojo', 29.99,
         'compasso', 6.69,
         'livro', 129.38,
         'mochila', 139.43,
         'caneta azul',  1.59,
         'caneta preta', 1.29)
print('-' * 40)
print(f'{"LISTA DE PREÇOS:":^40}')
print('-' * 40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R$ {lista[i]:>7.2f}')  
print('-' * 40)