n = int(input('digite o numero para obter seu fatorial'))
c = n
f = 1
print(f'{n}! = ', end='')
while c != 0:
    print(f'{c} -> ', end='')
    f *= c
    c -= 1
print(f'{f}')