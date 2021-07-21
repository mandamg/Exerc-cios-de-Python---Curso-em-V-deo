from random import randint
n = randint(0,10)
p = 0
r = -1
print('Digite o numero que eu pensei:')
while r != n:
        r = int(input('Qual seu palpite?'))
        p += 1
        if n < r:
            print('menos, tente novamente.')
        if n > r:
            print('mais, tente novamente.')
print(f'Você acertou eu pensei no numero {r}.  Você usou {p} palpites.')