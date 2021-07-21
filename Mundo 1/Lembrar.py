frase = 'Curso em Video'
print(frase[8:])
print(len(frase))
print(frase.count('e'))
print(frase.count('o', 0,13))
print(frase.find('deo'))
print(frase.rfind('o'))
print(frase.find('android'))
print('curso' in frase)
print(frase.replace('curso','android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
fala = '  Aprenda Python   '
print(fala)
print(fala.strip())
print(fala.rstrip())
print(fala.lstrip())
print(fala.split()) #estudar split
print('-'.join(fala))
divisor = fala.split()
print('-'.join(divisor))
###print
print('Em linguística, a noção de texto é ampla e ainda aberta')
print('a uma definição mais precisa. Grosso modo, pode ser entendido ')
print('como manifestação linguística das ideias de um autor,')
print('que serão interpretadas pelo leitor de acordo com seus conhecimentos')
print('linguísticos e culturais. Seu tamanho é variável.')

print('''Em linguística, a noção de texto é ampla
e ainda aberta a uma definição mais precisa. 
Grosso modo, pode ser entendido como manifestação linguística
das ideias de um autor, que serão interpretadas pelo leitor de acordo
com seus conhecimentos linguísticos e culturais. Seu tamanho é variável.''')
