f1 = input('Digite a frase')
f2 = f1.strip().replace(' ', '')
f3 = f2[::-1]
if f2 == f3:
    print(f'A frase "{f1}" é um palíndromo')
else:
    print(f'A frase "{f1}" não é um palíndromo.')