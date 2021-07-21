letra = 'BANCO POBRE'
print('-'*30)
print(f'{letra:-^30}')
print('-'*30)
s = int(input('Qual valor deseja sacar? '))
tudo = s
nota = 50
total= 0
while True:
    if tudo >= nota:
        tudo -= nota
        total += 1
    else:
        if total > 0:
            print(f'Você receberá {total} notas de R$ {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total = 0
        if tudo == 0:
            break
print('='*30)