import random

a1 = str(input("Nome do Aluno 1: "))
a2 = str(input("Nome do Aluno 2: "))
a3 = str(input("Nome do Aluno 3: "))
a4 = str(input("Nome do Aluno 4: "))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print(f"A ordem de apresentação é:{lista}")
