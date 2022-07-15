print('Aluguel de Carros')
d = int(input('Por Quantos Dias o carro foi alugado ?'))
k = float(input('Quantos KM ele Percorreu ?'))
print('Devido a quantidade de {} Dias e {} KM percorridos, o valor do Alugel sera de R$:{}'.format(d,k,(d*60)+(k*0.15)))
