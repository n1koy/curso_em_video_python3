# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezenas: 3
# Centenas: 8
# Milhas: 1

# num = int(input('Digite um número de 0 a 9999: '))
# n = str(num)
#print('Analisando o número {} temos que:'.format(num))
# print('Unidades: {}'.format(n[3]))
# print('Dezenas: {}'.format(n[2]))
# print('Centenas: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))

# Só funcionaria se digitar 4 digitos ou usando estrutura de repetição

num = int(input('Digite um número de 0 a 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {} temos que:'.format(num))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))





