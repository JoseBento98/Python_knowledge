#leitura de triangulos
# ñ consegui fazer
print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)
r1 = float(input('Primeiro Seg: '))
r2 = float(input('Segundo seg:'))
r3 = float(input('Terceito seg: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os seguimentos acima podem formar triangulos!')
else:
    print('Os Seguimentos acima não forman um triangulo: ')
