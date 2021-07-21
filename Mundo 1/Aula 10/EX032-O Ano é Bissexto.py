from datetime import date
n = int(input('Digite o ano: '))
if n == 0:
    n = date.today().year
if n%4 == 0 and n%100 !=0 or n%400 == 0:
    print(f'{n} é um ano bissexto')
else:
    print(f'{n} não é um ano bissexto')
