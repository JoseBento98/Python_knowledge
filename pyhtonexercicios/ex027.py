#primeiro e ultimo Nome
name = str(input('Digite Seu Nome: ')).strip()
print('Seu nome é {}'.format(name))
nl = name.split()
print('Seu Primeiro Nome nome é: {}'.format(nl[0]))
print('Seu Ultimo Nome é:{}'.format(nl[len(nl)-1]))


