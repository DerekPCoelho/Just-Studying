time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('nome do jogador:  '))
    total = int(input(f'\nTotal de partidas jogadas por {jogador["nome"]}  ? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Total de gols marcados? {c+1}')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('gostaria de adicionar um jogador? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro, resposta invalida!')
    if resposta == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end ='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
print('-=' * 30)
while True:  
    busca = int(input('Qual Jogador? (999 para encerrar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! NUMERO INVALIDO {busca}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]} :')
        for i , g in enumerate(time[busca] ['gols']):
            print(f'   {i} fez {g} gols. ')
    print('-=' * 30)   
print('VOLTE SEMPRE!')     
               