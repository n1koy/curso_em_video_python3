# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#nome = str(input('Digite aqui um nome: ')).strip().split()
#verif = 'SILVA' in nome
#print('O nome {} tem a palavra Silva? {}'.format(nome,verif))

nome = str(input('Digite aqui um nome: '))
nome1 = nome.upper().strip().split()
verif = 'SILVA' in nome1
print('O nome {} tem a palavra Silva? {}'.format(nome,verif))