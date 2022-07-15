#se o nome de uma cidade começa com santo
city = str(input('Digite o nome de uma Cidade: ').strip())
print(city[:5].upper() == 'SANTO')