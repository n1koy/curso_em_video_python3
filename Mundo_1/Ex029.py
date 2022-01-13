# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h
# Mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

km = int(input('Qual a velocidade atual do carro? '))
multa = (km-80)*7
if km >80:
    print('Você foi multado. Você excedeu o limite permitido que é de 80Km/h')
    print('O valor da multa é de R$7,00 por cada Km acima do limite')
    print('O valor da multa a pagar é de R${:.2f}'.format(multa))
print('='*50)
print('Dirija com segurança!')
print('='*50)

from random import randint
from time import sleep
print('Seu carro passou no radar 🚗...')
sleep(3)
vel = randint(20,160)
if vel > 80:
    print('Você estava a {}Km/h e foi multado! O valor da multa é R${:.2f}'.format(vel, (vel-80)*7))
else:
    print('Sua velocidade é {}Km/h, continue respeitando os limites.'.format(vel))