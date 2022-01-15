''' Desafio 28:

Problema: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
          E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.
          
Resolução:
'''

import random
import time
pc = random.randint(1,10)
print('O computador escolheu um número secreto entre 1 e 10. Tente adivinhar o número escolhido')
print('='*50)
jogador = int(input('Digite aqui o número que você acha que o computador escolheu: '))
print('='*50)
print('Processando...')
print('='*50)
time.sleep(2)
if jogador == pc:
    print('\033[1;32mParabens!!! Você acertou o número!!')
else:
    print('\033[1;31mVocê não acertou. O número que o computador escolheu foi o {}'.format(pc))
