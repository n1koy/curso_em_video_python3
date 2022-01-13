# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#salario = float(input('Digite o valor do seu salário: R$'))
#if salario >1250:
 #   print('Você ganhou um bônus de R${:.2f} conforme o aumento de 10% no valor base R${:.2f}. Logo o seu salário atual é de R${:.2f}'.format(salario*10/100, salario, salario*10/100+salario))
#else:
 #   print('Você ganhou um bônus de R${:.2f} conforme o aumento de 15% no valor base R${:.2f}. Logo o seu salário atual é de R${:.2f}'.format(salario*15/100, salario, salario*15/100+salario))

salario = float(input('Digite o valor do salário: R$'))
if salario <=1250:
    bonus = salario * 15 / 100
    novo = salario + bonus
    porcento = ('15%')
else:
    bonus = salario * 10 / 100
    novo = salario + (salario * 10 / 100)
    porcento = ('10%')
print('O funcinário ganhou um bônus de R${:.2f} por causa do aumento de {} no valor base do salário atual R${:.2f}. Logo com o reajuste o funcionário ganhará um salário de R${:.2f}'.format(bonus, porcento, salario, novo))
