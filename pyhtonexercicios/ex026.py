#procura letras
text = str(input('Digite um Texto Qualquer: ')).lower().strip()
print('A Letra A aparece {} vezes na frase.'.format(text.count('a')))
print('A Primeira letra A apareceu na posição {}'.format(text.find('a')+1))
print('A Ultima letra A apareceu na posição {}'.format(text.rfind('a')+1))
