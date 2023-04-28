ficha = list()
while True:
    nome = str(input("\nNome do aluno: "))
    notav1 = float(input('\nDigite a nota da V1: '))
    notav2 = float(input('\nDigite a nota da V2: '))
    media = (notav1 + notav2) / 2
    ficha.append([nome, [notav1, notav2], media])
    continuar = str(input('\nGostadia de adicionar um novo aluno? [S/N] '))
    if continuar in 'Nn':
        break
print('-=' * 15)
print(f'{"No.":<4}{"Nome:":<10}{"Média:":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-' * 35)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opção == 999:
        print('FINALIZANDO....')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção] [0]} : {ficha[opção] [1]} ')
    print('Volte sempre!')
        