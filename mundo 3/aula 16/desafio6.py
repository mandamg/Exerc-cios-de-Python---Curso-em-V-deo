a = 'abacaxi', 'acerola', 'hamburguer'
for b in a:
    print(f'\nna palavra {b.upper()} temos ', end='')
    for letra in b:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')