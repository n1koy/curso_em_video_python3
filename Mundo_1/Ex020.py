""" Desafio 020:

Problema: O mesmo professor do desafio 019 quer sortear a ordem
          de apresentação de trabalhos dos alunos. Faça um programa
          que leia o nome dos quatro alunos e mostre a ordem sorteada.
          
Resolução do problema:
"""

import random

al1 = input('Digite o nome do primeiro aluno: ').strip().capitalize()
al2 = input('Digite o nome do segundo aluno: ').strip().capitalize()
al3 = input('Digite o nome do terceiro aluno: ').strip().capitalize()
al4 = input('Digite o nome do quarto aluno: ').strip().capitalize()
alunos = [al1,al2,al3,al4]
random.shuffle(alunos)
print('A ordem de apresentação das equipes vai ser: {}'.format(alunos))

