# from random import sample
# numeros = (sample(range (0,11), 5))
# print(f'a sequencia de 5 numeros: {numeros}')
# print(f'o maior numero é: {max(numeros)}')
# print(f'o menor numero é: {min(numeros)}')


from random import randint
numero = (randint(0,11), randint(0,11), randint(0,11), randint(0,11), randint(0,11))
for c in range (0,5):
    print(numero[c], end = ' ')
print(f'\nmaior valor {max(numero)}')
print(f'maior valor {min(numero)}')