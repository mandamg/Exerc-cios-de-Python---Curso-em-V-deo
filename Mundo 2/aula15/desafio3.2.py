from random import randint
v = 0
while True:
    jg = int(input('Digite o numero que deseja jogar: '))
    pc = randint(0 , 10)
    total = jg + pc
    ip = ' '
    while ip not in 'IP':
        ip = input('Você quer Ímpar ou Par? [I/P]').upper()
    print(f'Você jogou {jg} e eu joguei {pc}, o total é {total}.')
    if ip == 'P':
        if total % 2 == 0:
            print('Deu par, você venceu!')
            v += 1
        else:
            print('Deu ímpar, você perdeu!')
            break
    if ip == 'I':
        if total %2 != 0:
            print('Deu ímpar, você venceu!')
            v += 1
        else:
            print('Deu par, você perdeu!')
            break
print(f'Você me venceu {v} vezes consecutivas. ')