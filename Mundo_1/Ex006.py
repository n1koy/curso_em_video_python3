""" Desafio 006:

Problema: Crie um algoritmo que leia um número e mostre o seu drobro,
          triplo e raiz quadrada.
          
Resolução do problema:
"""


n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)
print('Analisando o número {}: \n- O seu dobro é: {} \n- Triplo: {} \n- Sua raiz quadrada é: {:.4}'.format(n,d,t,rq))


"""   Extra:
              """

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# s = n1+n2
# m = n1*n2
# d = n1/n2
# di = n1//n2
# r = n1%n2
# p = n1**n2
# rq = s**(1/2)
# print('A soma dos valores é {}, enquanto a multiplicação é {} e a divisão é {:.3f}'.format(s,m,d))
# print('A divisão inteira é {} e o resto da divisão é {}'.format(di,r))
# print('A potência dos valores é {}'.format(p))
# print('A raiz quadrada de {} é {:.3f}'.format(s,rq))

