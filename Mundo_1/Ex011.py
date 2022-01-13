# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade de tinta necessaria para pintá-lo
# Sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Digite aqui a altura da pareda: '))
largura = float(input('Digite aqui a largura da parede: '))
area = altura*largura
litros = area/2
print('Uma parede com dimensões de {}x{} tem uma área de {:.2f}m² \nLogo para pintar essa parede você precisará de {:.2f} litros de tinta'.format(altura,largura,area,litros))