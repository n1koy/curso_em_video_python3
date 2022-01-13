# Faça um programa que leia o nome completo de uma pessoa
# Mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite aqui seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {} '.format(nome[-1]))
