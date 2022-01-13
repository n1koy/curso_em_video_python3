""" Desafio 003:

Problema: Crie um programa que leia dois números e mostre a soma entre eles.

Resolução do problema:
"""

n1 = int(input('\033[1;31mDigite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1+n2
print('\033[0;35mA soma entre \033[4;33m{} e {}\033[m \033[35mvale \033[4;36m{}'.format(n1,n2,soma))
