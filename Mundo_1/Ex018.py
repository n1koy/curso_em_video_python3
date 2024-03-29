""" Desafio 018:

Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.
          
Resolução do problema:
"""

from math import cos, sin, tan, radians

ang = float(input('Digite o valor de um ângulo qualquer: '))
print('Analisando o ângulo de {}°, temos que: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))

