""" Desafio 011:

Problema: Faça um programa que leia a largura e a altura de uma
          parede em metros, calcule a sua área e a quantidade de
          tinta necessária para pintá-la, sabendo que cada litro
          de tinta pinta uma área de 2 metros quadrados.
          
Resolução do problema:
"""

altura = float(input('Informe a altura da pareda: '))
largura = float(input('Informe a largura da parede: '))
area = altura*largura
litros = area/2
print('Uma parede com dimensões de {}x{} tem uma área de {:.2f}m² \nLogo para pintar essa parede você precisará de {:.2f} litros de tinta'.format(altura,largura,area,litros))
