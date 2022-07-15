#Strings
n = str(input('Digite seu Nome Completo'))
print('Tudo UP:{} '.format(n.upper()))
print('Tudo Lower:{}'.format(n.lower()))
print('Quantas Letras tem: {}'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
divite = n.split()
print('Seu primeiro nome é {} e ele tem tem {} letras.'.format(divite[0], len(divite[0])))
#+ pratica + logica - sono 

