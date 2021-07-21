nome = str(input('Digite seu nome completo: '))
s = nome.split()
f = s[::-1]
print(f'prazer conhece-lo!\nSeu primeiro nome é {s[0]}\nSeu sobrenome é {f[0]}')