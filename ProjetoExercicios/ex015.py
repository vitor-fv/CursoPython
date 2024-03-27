m = int(input('Quantos Km foram percorridos? '))
d = int(input('Quantos dias foram alugados? '))

#valor_m = m * 0.15
#valor_d = d * 60
#t = valor_m + valor_d

t = (m * 0.15) + (d * 60)
print('Preço a pagar pelo aluguel é de R$: {:.2f}'.format(t))
