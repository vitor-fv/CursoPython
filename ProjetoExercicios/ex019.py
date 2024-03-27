from random import choice
a1 = str(input("Nome do Aluno 1: "))
a2 = str(input("Nome do Aluno 2: "))
a3 = str(input("Nome do Aluno 3: "))
a4 = str(input("Nome do Aluno 4: "))

#alunos = []
#qtd_Alunos = int(input("Insira a quantidade de alunos: "))

#for i in range(0,qtd_Alunos):
    #nome_aluno = input("Digite o nome do aluno: ")
    #alunos.extend([nome_aluno])
    #print (alunos)

lista = [a1,a2,a3,a4]
#sorteio = choice(alunos)
sorteio = choice(lista)
print('O aluno que irá limpar o quadro será: {}'.format(sorteio)
