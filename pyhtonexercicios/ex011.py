#leia largura e altura de uma parede e saber quanto de tinta usa
print('parede teste')
l = float(input('Quanto tem de Largura :'))
a = float(input('Quanto tem de Altura :'))
balde = 2**2
print('o Tamanho da Area e de: {} m2\n cada Balde pode pintar: {} m2\n Logo Você Precisará de {} Baldes'.format(l*a,balde,(l*a)/balde))

