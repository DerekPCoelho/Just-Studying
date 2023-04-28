soma = 0
media = 0
idade_do_homem_mais_velho = 0
nome_do_homem_mais_velho = 0
total_mulheres_menor_de_20 = 0

for p in range(1, 5):
    print('------ {}ª pessoa------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma = soma + idade
    if p == 1 and sexo in 'Mn':
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
    if sexo in 'Mm' and idade > idade_do_homem_mais_velho:
         idade_do_homem_mais_velho = idade
         nome_do_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres_menor_de_20 +=1
media = soma / 4       
print('O grupo possui uma media de idade de: {} anos !'.format(media))
print('O homem mais velho no grupo, se chama {}`e possui {} anos!'.format(nome_do_homem_mais_velho,idade_do_homem_mais_velho )) 
print('O total de mulheres com menos de 20 anos no grupo é de: {}'.format(total_mulheres_menor_de_20))  