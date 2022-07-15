#calculador de viagens
distance = float(input('What is the Distance in KM? '))
if distance <= 200:
    print('The Value of your Ticket is:${}'.format(distance*0.50))
else:
    print('The Value of Your ticket is:${} '.format(distance*0.45))
print('The End!')
