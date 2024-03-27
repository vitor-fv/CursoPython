#import random

from random import shuffle

alunos = []
qtd_Alunos = int(input("Insira a quantidade de alunos: "))
numero_sorteado = 0

for i in range(0,qtd_Alunos):
    nome_aluno = input("Digite o nome do aluno: ")

    alunos.extend([nome_aluno])
    #print (alunos)

#sorteio = choice(alunos)
sorteio = shuffle(alunos)
print (alunos)
#print('O aluno que irá limpar o quadro será: {}'.format(sorteio))