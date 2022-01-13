#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# from math import trunc
# num = float(input('Digite um número com várias casas decimais: '))
# print('A porção inteira do número {} é {}'.format(num,trunc(num)))

num = float(input('Digite um número: '))
print('A porção inteira do número {} é {}'.format(num,int(num)))