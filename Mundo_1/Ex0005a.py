# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n = int(input('\033[4;35mDigite um número: \033[m'))
suc = n+1
ant = n-1
print('\033[31mO número digitado é \033[33m{}\033[31m, sendo seu \033[4msucessor\033[m \033[31mo número \033[33m{}\033[31m e \033[4mantecessor\033[0;31m o número \033[33m{}'.format(n,suc,ant))