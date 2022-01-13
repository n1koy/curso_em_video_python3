""" Desafio 019:

Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.
          
Resolução do problema:
"""

import random

al1 = input('Digite o nome do aluno: ')
al2 = input('Digite o nome do aluno: ')
al3 = input('Digite o nome do aluno: ')
al4 = input('Digite o nome do aluno: ')
lista = [al1,al2,al3,al4]
sorteio = random.choice(lista)
print('O aluno esoclhido foi o(a) {}'.format(sorteio))
