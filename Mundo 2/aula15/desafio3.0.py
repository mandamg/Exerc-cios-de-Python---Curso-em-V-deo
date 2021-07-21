from random import randint
p = s =0
while True:
    n = int(input('Digite o numero: '))
    e = ' '
    while e not in 'PI':
        e = input('Você quer PAR ou ÍMPAR?[P/I]').upper()
    pc = randint(0,10)
    o = pc + n
    if o % 2 == 0 and e == 'P':
        print('='*30)
        print(f'Você jogou {n} e eu joguei {pc} o resultado é {o}.\nDeu par, você venceu.\nVamos jogar de novo!')
        print('=' * 30)
        p += 1
    elif o % 2 != 0 and e == 'I':
        print('=' * 30)
        print(f'Você jogou {n} e eu joguei {pc} o resultado é {o}.\nDeu ímpar, você venceu.\nVamos jogar de novo!')
        print('=' * 30)
        p += 1
    elif o % 2 != 0 and e == 'P':
        print('='*30)
        print(f'Você jogou {n} e eu joguei {pc} o resultado é {o}.\nDeu ímpar, eu venci.')
        print(f'Vc me venceu {p} vezes consecutivas.')
        break
    else:
        print('=' * 30)
        print(f'Você jogou {n} e eu joguei {pc} o resultado é {o}.\nDeu par, eu venci.')
        print(f'Vc me venceu {p} vezes consecutivas.')
        break
