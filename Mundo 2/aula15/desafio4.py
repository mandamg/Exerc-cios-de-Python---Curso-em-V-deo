legal = male = female = 0
while True:
    print('-'*30)
    age = int(input('Age: '))
    genre = ' '
    while genre not in 'MF':
        genre = input('Genre [M/F]: ').upper()
    print('-'*30)
    if age >= 18:
        legal += 1
    if genre == 'M':
        male += 1
    elif genre == 'F' and age <= 20:
        female += 1
    cont = ' '
    while cont not in 'YN':
        cont = input('Do you want to continue? [Y/N]').upper()
    print('-'*30)
    if cont == 'N':
        break
print(f'{legal} são maiores de 18.')
print(f'{male} são homens.')
print(f'{female} são mulheres abaixo de 20 anos.')