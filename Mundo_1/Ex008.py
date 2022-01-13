""" Desafio 007:

Problema: Desenvolva um programa que leia as três notas de um aluno,
          calcule e mostre a sua média.
          
Resolução do problema:
"""

al = input('Digite o nome do aluno: ').strip()
n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
n3 = float(input('Digite a nota da terceira prova: '))
me = (n1+n2+n3) / 3
print('A média das notas do aluno "{}" foi de {:.2f} pontos'.format(al.capitalize(),me))
