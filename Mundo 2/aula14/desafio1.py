sexo = input('Digite seu sexo[M/F]:').upper()
while sexo not in 'MmFf':
    sexo = input('Digite novamente').upper()
idade = input('Digite sua idade:')
print('registrado com sucesso')