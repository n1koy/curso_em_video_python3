# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

cliente = input('Nome do cliente que alugou o carro: ')
dias = int(input('Por quantos dias o cliente alugou o carro: '))
km = float(input('Quantos km o cliente rodou: '))
preço = (60*dias)+(0.15*km)
print('O cliente "{}" alugou o carro por {} dias e rodou um total de {:.2f}km. Portanto o valor a pagar do aluguel é de R${:.2f}'.format(cliente,dias,km,preço))