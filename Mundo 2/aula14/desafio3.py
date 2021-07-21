n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
op = 0
maior = 0
while op != 5:
    op = int(input('Qual operação deseja realizar?\n[1] soma\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] fechar programa\n'))
    print('=' * 25)
    if op != 5:
        if op == 1:
            print(f'o resultadoo da soma é {n1+n2}')
            print('='*25)
        elif op == 2:
            print(f'o resultado da multiplicação é {n1*n2}')
            print('=' * 25)
        elif op == 3:
            if n1 > n2:
                maior = n1
            elif n2 > n1:
                maior = n2
            else:
                print('Os valores são iguais')
            print(f'o maior valor é {maior}')
            print('=' * 25)
        elif op ==4:
            n1 = int(input('Digite um valor:'))
            n2 = int(input('Digite um valor:'))
print('FIM.')
