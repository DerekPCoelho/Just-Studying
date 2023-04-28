print('''
      Bem vindo(a) a sua calculadora!

    Para iniciarmos, escolha dois numeros! 
''')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opção = 0
while opção != 8:
    print('''
=========================================
          
Selecione a operação que deseja executar:

          [ 1 ] Multiplicação
          [ 2 ] Soma
          [ 3 ] Subtração
          [ 4 ] Divisão
          [ 5 ] Maior
          [ 6 ] Menor
          [ 7 ] Novos Números
          [ 8 ] Sair do Programa 
          
=========================================
''')
    opção = int(input('Opção: '))
    if opção == 1:
        produto = n1 * n2
        print('o resultado da multiplicação de {} por {} é: {}'.format(n1, n2, produto))
    elif opção == 2:
        soma = n1 + n2
        print('o resultado da soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif opção == 3:
        subtração = n1 - n2
        print('o resultado da subtração de {} e {} é: {}'.format(n1, n2, subtração))
    elif opção == 4:
        divisão = n1 / n2
        print('o resultado da divisão de {} por {} é: {:.2f}'.format(n1, n2, divisão))   
    elif opção == 5:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o maior numero é o {}'.format(maior))
    elif opção == 6:
        if n1 < n2:
            menor = n1
        else:
            menor = n2
        print('o menor numero é o {}'.format(menor))
    elif opção == 7:
        print('''
      Bem vindo(a) a sua calculadora!

    Para iniciarmos, escolha dois numeros! 
''')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
