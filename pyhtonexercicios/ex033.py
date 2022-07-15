# Maior e Menor de 3
#ñ consegui fazer
a = int(input('primeiro Numero: '))
b = int(input('segundo Numero: '))
c = int(input('terceito Numero: '))
#verificando Menor
menor = a
if b < a and b < c:
      menor = b
if c < a and c < b:
      menor = c
#verificando Maior
maior = a
if b > a and b > c:
      maior = b
if c > a and c > b:
      maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor Digitado foi {}'.format(maior))
