# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite aqui uma frase qualquer: ')).upper().strip()
letra = frase.count('A')
prim = frase.find('A')+1 # +1 pq o python cmeça a contar do 0
ult = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase'.format(letra))
print('A primeira letra A apareceu na posição {}'.format(prim))
print('A última letra A apareceu na posição {}'.format(ult))

