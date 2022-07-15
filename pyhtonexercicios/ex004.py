a = input('Escreva Algo:')  # o tipo primitivo vem antes do input
print('O tipo primitivo deste valor é', type(a))  # todo tipo primitvo que não for especificado sera STR
print(a, 'Só Tem Espaço?', a.isspace())
print(a, 'é um numero?', a.isnumeric())
print(a, 'é alfabetico ?', a.isalpha())
print(a, 'é AlfaNumerico ?', a.isalnum())
print(a, 'Esta em Maiusculas ?', a.isupper())
print(a, 'Esta em Minusculas?', a.islower())
print(a, 'Está Capitalizada ?', a.istitle())  # capitalizada é  um texto Formal
