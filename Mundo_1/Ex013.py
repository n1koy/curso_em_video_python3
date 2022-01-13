""" Desafio 013:

Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento.
          
Resolução do problema:
"""

funcionario = input('Digite o nome do funcionário: ')
salario = float(input('Digite aqui o sálario do funcionário: R$'))
descont = (salario*15)/100
novo = salario+descont
print('Com um acrescimo de 15%, o salario base (R${:.2f}) do funcionário {} aumentará em R${:.2f}. Então com o reajuste seu novo salario será de: R${:.2f}'.format(salario,funcionario,descont,novo))
