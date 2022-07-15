print('Testando Conhecimentos')
a = input('Digite algo para iniciar os testes:' )
print('Tente',a,'iniciado com Sucesso!')
n1 = float(input('Numero Normero para saber suas operações Numericas: '))
n2 = float(input('Digite um Segundo Numero para saber Operações Numericas: '))
p = float(input('Digite uma Potencia para se aplicar: '))
from random import sample
print('='*25)
lista = print('Sua Soma é: ',n1 + n2),\
    print('Sua Subtração é: ',n1 - n2),\
    print('Sua Divisão é: ',n1 / n2),\
    print('Sua Multiplicação é: ', n1 * n2),\
    print('suas potencias são: ', n1 **p,n2 ** p),\
    print('Sua Divisão Inteira é: ',n1 // n2),\
    print('O resto de sua divisão e: ',n1 % n2),\
    print('as Suas Raizes são: ',n1 ** (1/2),n2 ** (1/2))
print('='*25)
print('Ultilizando a biblioteca Ramdom com comando sample fará uma lista aleatoria')
print(sample(lista,k=7))
print('+'*25)
n3 = float(input('Digite um Numero para o test Math'))
from math import ceil, floor, trunc, pow, sqrt, factorial
print('De Acordo com math o resultado sera:')
lista1 = print('arredond p/ cima: ',ceil(n3)),\
    print('arredond p/ baixo: ',floor(n3)),\
    print('Corte de Virgula: ',trunc(n3)),\
    print('Sua Potencia e: ',pow(n3,p)),\
    print('Sua Raiz Quadrad:',sqrt(n3))
print('Voltando ao Ramdom',sample(lista1,k=5))
print('+'*25)
print('Os Numeros do Primeiro teste foram',n1 ,'e',n2,'e o numero para o terceiro teste foi',n3,)
print('Paa todos os testes a potencia foi: ',p)
#falhas no imput do ramdom
#nem um uso do .format() {}
# melhorar esses quesitos e a syntax
