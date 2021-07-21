a = (int(input('Digite um valor: ')),
    int(input('Digite segundo valor: ')),
    int(input('Digite terceiro valor: ')),
    int(input('Digite quarto valor: ')))
print(f' voce digitou os valores: {a}')
print(f'o nove foi digitado {a.count(9)} vezes.')
if 3 in a:
    print(f'o primeiro três digitado aparece na {a.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print(f'o total de numeros pares é ', end='')
for n in a:
    if n % 2 == 0:
      print(n, end=' ')
