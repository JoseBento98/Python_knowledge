#aumento salarial
print(' Aumento de 15% salarial')
n1 = float(input('Digite seu Salario para um aumento de 15% :'))
f = (15*n1)/100
vf = n1+f
print('Seu Salario agora é :',vf)
#Utilizar + o .format()
s = float(input('Qual é o Salario do Funcionario ? R$:'))
novo = s + (s * 15 / 100)
print('Um Funcionario que ganhava R$:{:.2f},com 15% de aumento, passa a receberR$:{:.2f}'.format(s,novo))
