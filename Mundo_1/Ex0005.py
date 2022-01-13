n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
r = n1%n2
p = n1**n2
rq = s**(1/2)
print('A soma dos valores é {}, enquanto a multiplicação é {} e a divisão é {:.3f}'.format(s,m,d))
print('A divisão inteira é {} e o resto da divisão é {}'.format(di,r))
print('A potência dos valores é {}'.format(p))
print('A raiz quadrada de {} é {:.3f}'.format(s,rq))