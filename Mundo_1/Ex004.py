""" Desafio 004:

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.
          
Resolução do problema:
"""


msg = input('Digite qualquer coisa: ')
print('\033[1;33mSegue abaixo as informações: \033[m')
print('\033[7;40mTipo primitivo:\033[m', '\033[1;36m', type(msg), '\033[m')
print('\033[7;40mAlfanúmerico:\033[m', '\033[1;36m', msg.isalnum(), '\033[m')
print('\033[7;40mAlfabético:\033[m', '\033[1;36m', msg.isalpha(), '\033[m')
print('\033[7;40mNumérico:\033[m', '\033[1;36m', msg.isnumeric(), '\033[m')