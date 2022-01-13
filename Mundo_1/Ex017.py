""" Desafio 017:

Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.
          
Resolução do problema:
"""

from math import hypot

catop = float(input('Digite o comprimento do cateto oposto de um triângulo retângulo: '))
catad = float(input('Difite o comprimento do cateto adjacente de um triângulo retângulo: '))
print('A medida da hipotenusa desse triângulo retângulo é {:.2f}'.format(hypot(catop,catad)))
