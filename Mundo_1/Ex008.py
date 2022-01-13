# Escreva um programa que leia um valor em metros e a exiba convertido em centimetros e milimetros

m = float(input('Digite uma distância em metros: '))
km = m/1000
cm = m*100
mm = m*1000
mi = m/1609
yd = m*1.094
ft = m*3.281
inch = m*39.37
print('A distância de {}m corresponde a: \n{}km\n{}cm\n{}mm\nConvertando para medidas EUA a distância de {}m corresponde a: \n{:.3f}mi\n{:.2f}yd\n{:.2f}ft\n{:.2f}inch'.format(m, km, cm, mm, m, mi, yd, ft, inch))