letra = 'BANCO POBRE'
print('-'*30)
print(f'{letra:-^30}')
print('-'*30)
s = int(input('Qual valor deseja sacar? '))
m = s // 50
r = s % 50
c = r // 20
r1 = r % 20
d = r1 // 10
r2 = r1 % 20
u = r2 // 1 %10
print('Você receberá:')
if m != 0:
    print(f'{m} notas de R$ 50')
if c != 0:
    print(f'{c} notas de R$ 20')
if d != 0:
    print(f'{d} notas de R$ 10')
if u != 0:
    print(f'{u} notas de R$ 1')



