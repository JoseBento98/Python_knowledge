#aumento de 2 salarios
s1 = float(input('Enter the wage: '))
if s1 >= 1250:
    print('your new wage is: {}'.format(s1 + (s1*10/100)))
else:
    print('your new wage is: {}'.format(s1 + (s1*15/100)))
print('the end!!!')
