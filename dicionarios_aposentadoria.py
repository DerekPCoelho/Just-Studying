from datetime import datetime
dados = dict()
dados['nome'] = str(input('\nNome: '))
nasc = int(input('\nAno Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('\nC L T, (0 caso nao tenha) : '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('\nano de contratação: '))
    dados['salario'] = float(input('\nseu salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print(dados)
for k, v in dados.items():
    print(f'  -{k} : {v}')