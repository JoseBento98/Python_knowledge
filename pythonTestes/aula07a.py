print ('Teste de Operadores Aritimeticos')
n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Numero: '))
a = n1 + n2
s = n1 - n2
d = n1 / n2
m = n1 * n2
p = n1 ** n2
di = n1 // n2
rd = n1 % n2
print('a Adição é: {}\na Subtração é: {}\na Divisão é: {:.2f} \na Multiplicação é: {} '.format(a,s,d,m),'')
print('a Potencia é: {}\na Divisão Inteira é: {}\no Resto da Divisão é: {}'.format(p,di,rd))
# posso formatar as mascaras {} ex: {:.3f} = indica que minha casa so poderá ter no maximo 3 casas flutuantes
# no final da linha do print posso colocar o comando ,end = ' ' ) para impedir a quebra de texto, posso escrever algo dentro para ' ' para sinalizar a quebra de texto
# posso tambem quebrar o texto onde eu quiser com /n





