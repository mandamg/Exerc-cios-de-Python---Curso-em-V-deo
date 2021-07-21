maior = 0
menor = 0
for c in range(1, 6):
    a = float(input('digite o peso:'))
    if c == 1:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print(f'o maior peso foi {maior}')
print(f'O menor peso é {menor}')