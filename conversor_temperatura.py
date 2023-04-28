print('''
      Bem vindo(a) ao conversor térmico!

    Para iniciarmos, digite apenas o valor da
    temperatura que deseja converter!!
     
''')
t = int(input('Temperatura: '))
opção = 0
while opção != 7:
    print('''
=========================================
          
Selecione a operação que deseja executar:

          [ 1 ] Celsius    -> Kelvin
          [ 2 ] Celsius    -> Fahrenheit
          [ 3 ] Kelvin     -> Celsius
          [ 4 ] Kelvin     -> Fahrenheit
          [ 5 ] Fahrenreit -> Celsius
          [ 6 ] Fahrenreit -> Kelvin
          
          [ 7 ] Sair do Programa 
          
=========================================
''')
    opção = int(input('Opção: '))
    if opção == 1: 
        tk = t + 273
        print(f'Esta temperatura equivale a : {tk:.0f}ºK')
    elif opção == 2:    
        tf = (t * 1.8) + 32
        print(f'Esta temperatura equivale a : {tf:.0f}ºF')
    elif opção == 3:   
        tc = t - 273
        print(f'Esta temperatura equivale a : {tc:.0f}ºC')
    elif opção == 5:   
        tf = 1.8 * (t - 273) + 32.
        print(f'Esta temperatura equivale a : {tf:.0f}ºF')
    elif opção == 4:    
        tc = (t - 32) * (5/9)
        print(f'Esta temperatura equivale a : {tc:.0f}ºC')
    elif opção == 6:
        tk = (t + 459.67) * (5/9)
        print(f'Esta temperatura equivale a : {tk:.0f}ºK')
print('PROGRAAMA FINALIZADO...')
