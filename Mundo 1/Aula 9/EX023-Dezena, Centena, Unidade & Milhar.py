n = int(input('digite um numero de 0 a 9999:'))
a = n // 1 % 10
b = n // 10 % 10
c = n // 100 % 10
d = n // 1000 % 10
print(f'o numero tem:\n{a} unidades')
print(f'{b} dezenas')
print(f'{(c)} centenas')
print(f'{d} milhar')