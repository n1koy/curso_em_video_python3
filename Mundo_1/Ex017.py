# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# import math

# catop = float(input('Digite o comprimento do cateto oposto de um triângulo retângulo: '))
# catad = float(input('Digite o comprimentodo cateto adjacente de um triângulo retângulo: '))
# hipot = math.hypot(catop, catad)
# print('O comprimento da hipotenusa desse triângulo retângulo é {:.2f}'.format(hipot))

from math import hypot

catop = float(input('Digite o comprimento do cateto oposto de um triângulo retângulo: '))
catad = float(input('Difite o comprimento do cateto adjacente de um triângulo retângulo: '))
print('A medida da hipotenusa desse triângulo retângulo é {:.2f}'.format(hypot(catop,catad)))