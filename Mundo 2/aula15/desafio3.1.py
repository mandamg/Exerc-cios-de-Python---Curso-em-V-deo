from random import randint
p = s = 0
while True:
    n = int(input('Digite o numero: '))
    e = input('Você quer PAR ou ÍMPAR?[P/I]').upper()
    pc = randint(0, 10)
    o = pc + n
    if o % 2 == 0 and e == 'P' or o % 2 != 0 and e == 'I':
        print('='*30)
        print(f'Você jogou {n} e eu joguei {pc} o resultado é {o}.', end= '')
        if o % 2 == 0:
            print(' Deu par, você venceu.\nVamos jogar de novo!')
        else:
            print(' Deu ímpar, você venceu.\nVamos jogar de novo!')
        print('=' * 30)
        p += 1

    else:
        print('=' * 30)
        print(f'Você jogou {n} e eu joguei {pc} o resultado é {o}.')
        if o % 2 == 0:
            print('Deu par, eu venci.')
        else:
            print('Deu ímpar, eu venci.')
        print(f'Vc me venceu {p} vezes consecutivas.')
        break