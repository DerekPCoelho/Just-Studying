def contador(i, f, p):
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end ='') 
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end ='')
            cont -= p
        print('fim')
    
contador(1, 100, 10)
contador(100, 1, 10)