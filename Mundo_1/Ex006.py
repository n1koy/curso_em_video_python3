# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)
print('Analisando o número {}: \n- O seu dobro é: {} \n- Triplo: {} \n- Sua raiz quadrada é: {:.4}'.format(n,d,t,rq))