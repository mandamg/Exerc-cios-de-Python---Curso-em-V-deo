a = int(input('digite um numero: '))
q = 0
for c in range(1,a+1):
    if a%c==0:
        print('\033[m', end=' ')
        q += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n{a} foi dividido {q} vzs')
if q == 2:
    print('ele é primo')
else:
    print('ele não é primo')