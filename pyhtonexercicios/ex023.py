# numero Aleatorio
'''primeiro metodo
print('Iniciando...')
n = str(input('Digite um Numero: '))
print('Sua unidade é:', (n[3]))
print('Sua Dezena é:', (n[2]))
print('Sua Centena é:', (n[1]))
print('Sua Milhar é:', (n[0])) '''

print('Iniciando...')
n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o Numero: {}'.format(n))
print('Sua Unidade é: {}'.format(u))
print('Sua Dezena é: {}'.format(d))
print('Sua Centena é: {}'.format(c))
print('Sua Milhar é: {}'.format(m))
# Formato da Aula 





