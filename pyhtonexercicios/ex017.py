#calculo de catetos
import math
co = float(input('Informe o Quadrado do Cateto Oposto: '))
ca = float(input('Informe o Quadrado do Cateto Adjsacente: '))
a2 = co**2
b2 = ca**2
# a função poseria ser feita se maneira + Logica
# ex: hi = (co**2 + ca**2 )**(1/2) [ pois toda potencia elevada a meia vira raiz ]
print(' a soma dos Catetos {}² e {}² e igual a Hypotenusa {:.2f}²'.format(co,ca,math.sqrt(a2+b2)))

# com a biblioteca math
#podemos utilizar a opção math.hypot(ca,co) e criar uma função para calcular a hypotenusa
# posso importar apenas 1 metodo
# ESTUDA SINTAXE POW
# ESTUDA AS FUNÇÕES DA BIBLIOTECA TBM



