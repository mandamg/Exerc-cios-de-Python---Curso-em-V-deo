from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = (date.today().year-ano - 18)*-1
if idade > 0:
    print(f'Ainda falta {idade} para seu alistamento obrigatorio')
elif idade == 0:
    print('Está na epoca que de se alistar!')
elif idade < 0:
    print(f'Já passou da epoca de se alistar. Você deveria ter se alistado há {idade*-1} anos')