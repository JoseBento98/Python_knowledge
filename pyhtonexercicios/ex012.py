#5% de desconto no produto
print(' Um desconto de 5%')
v = float(input('Valor do Produto :'))
d = (v/100)*5
vf = v - d
print('o valor do produto com desconto é de :', vf)
print('O Produto com Valor de R$: {:.2f} , receberá o Desconto de R$:{:.2f}\nTotalizando em R$:{:.2f}'.format(v,d,vf))
#Segundo Print Muito Melhor a Sintaxe
#tbm pode ser indicado pela seguinte função
p = float(input('Qual o Preço do Produto? R$:'))
novo = p - (p * 5 / 100) #Melhor Formula de Porcentagem
print('O Produto que Custava R$:{:.2f}, na promoção com 5% de desconto vai custar R$:{:.2f}'.format(p,novo))
