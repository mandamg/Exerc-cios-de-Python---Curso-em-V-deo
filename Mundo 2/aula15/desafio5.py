soma = p = c = m = 0
texto = 'LOJA DA HINA'
n = ' '
print(f'{texto:❤^40}')
while True:
    prod = input('Qual o nome do produto? ')
    prec = float(input('Qual o valor? '))
    soma += prec
    c += 1
    if c == 1:
        m = prec
        n = prod
        if m > prec:
            m = prec
            n = prod
    if prec > 1000:
        p += 1
    cont = ' '
    while cont not in 'SsNn':
            cont = input('Deseja continuar [S/N]? ').upper()
    if cont == 'N':
        break
print('='*45)
print(f'O valor total é: R${soma:.2f}')
print(f'O produto mais barato é {n}, ele custa R${m}')
print(f'Há {p} produtos acima de R$1000')
