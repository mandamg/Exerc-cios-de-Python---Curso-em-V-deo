import random
n1= input('nome do aluno')
n2 = input('nome do aluno')
n3 = input('nome do aluno')
n4 = input('nome do aluno')
list = [n1, n2, n3, n4]
random.shuffle(list)
print('A ordem da lista de alunos será: ')
print(list)