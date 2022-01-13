# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

# city = str(input('Digite o nome de uma cidade: '))
# print('SANTO' in city.upper())

cidade = input('Digite a cidade em que você nasceu: ').strip().capitalize()
print('A cidade {} começa com a palavra Santo? {}'.format(cidade, cidade[:5] == 'Santo'))

