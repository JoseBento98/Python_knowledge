# Condições
import random
import time

print('-=-' * 20)
print('Adivinhe que Número estou a Pensar...')
print('-=-' * 20)
number = int(input('Faça Sua Escolha de 1 a 5..: '))
n = random.randint(1, 5)
print('PROCESSANDO...')
time.sleep(3)
if number == n:
    print('Correto!')
else:
    print('Errado eu pensei no numero: {}'.format(n))
