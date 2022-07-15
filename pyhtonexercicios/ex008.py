#metros em centimetros e Milimetros
print('Transformador de Metros em Centimetros e Milimetros')
n1 = float(input('Digite o Valor em Metros: '))
print('Seu Valor em Centimentros é:',n1*100,'cm')
print('Seu Valor em Milimetros é: ',n1*1000,'mm')
#Melhorando o Desafio
print('Todas as Medidas!')
m = float(input('Digite um Valor em Metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('Sua Medida em Quilômetro é: {}\nSua Medida em Hectômetro é: {}\nSua Medida em Decâmetro é: {}'.format(km,hm,dam))
print('Sua Medida em Decímetro é: {}\nSua Medida em Centímetro é: {}\nSua Medida em Milímetro é: {}'.format(dm,cm,mm))



