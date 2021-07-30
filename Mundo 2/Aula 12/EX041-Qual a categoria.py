from datetime import date
i = int(input('Digite o ano de nascimento:'))
m = date.today().year - i
print(f'Voce tem {m}.')
if m <= 9:
    print('Sua categoria é mirim')
elif m <= 14:
    print('Sua categoria é infantil')
elif m <= 19:
    print('sua categoria é junior')
elif m <=25:
    print('Sua categoria é sênior')
else:
    print('Sua categoria é master')