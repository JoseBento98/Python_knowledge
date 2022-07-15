#velocidade de carro
velocit = float(input('Qual foi a velocidade? '))
print('Analisando...')
if velocit > 80:
    print('Você foi Multado em R${} por Excesso de Velocidade!'.format((velocit-80)*7))
else:
    print('Esta Liberado!')
