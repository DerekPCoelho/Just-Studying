n = str(input('Digite seu nome')).upper().strip()
nome = n.split()
print('primeiro nome: {}'.format(nome[0]))
print('ultimo nome: {}'.format(nome[len(nome)-1]))