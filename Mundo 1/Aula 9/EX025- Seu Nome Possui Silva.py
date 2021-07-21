nome = input('digite seu nome completo').upper()
s = 'SILVA' in nome
print(f'o nome possui silva? {(s)}')
if s == False:
    print('Seu nome não possui "Silva"')
if s == True:
    print('Seu nome possui "Silva"')
#b = nome.upper().find('SILVA')
#if b < 0 :
#    print('Seu nome não possui "Silva"')
#if b > 0:
#    print('Seu nome possui "Silva"')