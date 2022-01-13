# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

import time

print('='*100)
print('Esse é um programa para descobrir se o número escolhido é PAR ou ÍMPAR')
print('='*100)
n = int(input('Escolha um número: '))
par = n % 2
print('='*50)
print('Processando...')
print('='*50)
time.sleep(2)
if par == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))


