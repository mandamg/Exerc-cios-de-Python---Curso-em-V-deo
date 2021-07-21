import random
a = input('digite o primeiro aluno')
b = input('digite o segundo aluno')
c = input('digite o terceiro aluno')
d = input('digite o quarto aluno')
list = [a, b, c, d]
print(f'O aluno sortedo foi {random.choice(list)}')