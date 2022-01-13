# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre em ordem sorteada

import random

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
alunos = [al1,al2,al3,al4]
random.shuffle(alunos)
print('A ordem de apresentação das equipes vai ser: {}'.format(alunos))

