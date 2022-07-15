import random
#lista sequencial de alunos
print( 'Ordem de Apresentação')
lista = input('Aluno(a): '),\
    input('Aluno(a): '),\
    input('Aluno(a): '),\
    input('Aluno(a): ')
print('Os Alunos que participaram do a apresentação são {}'.format(lista))
print('A Apresentação acontecera na sequencia : {} '.format(random.sample(lista,k = 4)))
#pode ser feito da sequinte maneira random.shuffle(lista) [ aprendido na aula ] modo mais psimples
# depois colcoar um print com a lista

