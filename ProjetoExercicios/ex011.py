largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede:  '))
area = largura * altura
tinta = area / 2
#print('O valor da área é {:.1} m², e a quantidade de tinta é {:.1} L'.format(area, tinta))
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f} L de tinta'.format(tinta))
