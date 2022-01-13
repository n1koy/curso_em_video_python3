""" Desafio 010:

Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
          na carteira e mostre quantos dólares ela pode comprar.

Cotação: $5.62
          
Resolução do problema:
"""

cart = float(input('Digite aqui quantos reais você tem na sua carteira: R$'))
dol = cart/5.62560
print('Com R${:.2f}, você pode comprar U${:.2f}'.format(cart,dol))
