# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite aqui seu nome completo: ')).strip()
letras1 = len(nome)-(nome.count(' '))
separa = nome.split()

print('Seu nome com letras maúscula é: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(letras1))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
