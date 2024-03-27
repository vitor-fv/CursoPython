salario = float(input('Digite o seu salário: R$ '))
novo_salario = salario + (salario * 15 / 100)
print('O seu salário é: R$ {:.2f}, e com o aumento de 15% será: R$ {:.2f}.'.format(salario, novo_salario))
