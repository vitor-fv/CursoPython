valor_produto = float(input('Digite o preço do produto: R$ '))
desconto = valor_produto - (valor_produto * 5 / 100)
print('O produto de valor: R$ {:.2f} , está com desconto de 5% está custando R$ {:.2f}.'.format(valor_produto, desconto))
