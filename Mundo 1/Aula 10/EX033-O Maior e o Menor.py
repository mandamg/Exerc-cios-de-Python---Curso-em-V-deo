n = int(input('Digite um numero: '))
m = int(input('Digite um numero: '))
o = int(input('Digite um numero: '))
maior = n
if m > n:
    maior = m
if o > n:
    maior = o
print(f'O maior numero é {maior}')
menor = n
if m<n:
    menor = m
if o < n:
    menor = o
print(f'O menor numero é {menor}')
