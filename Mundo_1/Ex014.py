""" Desafio 014:

Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit.
          
Resolução do problema:
"""

celsius = float(input('Informe a temperatura em °C: '))
fah = (celsius*9/5)+32
print('A temperatura de {:.1f}°C corresponde a {:.2f}°F'.format(celsius,fah))
