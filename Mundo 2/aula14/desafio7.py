fn = int(input('Até onde a sequencia deve ir: '))
t1 = 0
t2 = 1
print(f'{t1} -> ', end='')
print(f'{t2} -> ', end='')
c = 3
while c <= fn:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1=t2
    t2=t3
    c+=1
print(' Fim.')
