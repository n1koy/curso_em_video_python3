# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

prod = float(input(('Digite aqui o preço do produto: R$')))
desc = (prod*5)/100
novo = prod-desc
print('O produto custava R${}, então você ganhará um desconto de R${:.2f} nesse produto. Logo seu valor final será de: R${:.2f}'.format(prod, desc, novo))