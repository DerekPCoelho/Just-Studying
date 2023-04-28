times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 
         'Atlético -GO')

print('-=' * 34)
print(f'\nLista de times: {times}\n')
print('-=' * 34)
print(f'\nOs 5 primeiros são: {times[0:5]}\n')
print('-=' * 15)
print(f'\nOs 5 ultimos são: {times[-4:]}\n')
print('-=' * 15)
print(f'\nEm ordem alfabética:{sorted(times)}\n')
print('-=' * 15)
print(f'\no corinthians está na {times.index("Corinthians")} posição!\n')
