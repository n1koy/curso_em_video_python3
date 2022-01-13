# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

al = input('Digite o nome do aluno: ')
n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
n3 = float(input('Digite a nota da terceira prova: '))
me = (n1+n2+n3) /3
print('A média das notas do aluno "{}" foi de {:.2f} pontos'.format(al,me))