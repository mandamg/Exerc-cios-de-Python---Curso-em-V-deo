l1 = int(input('Digite o tamanho de um lado: '))
l2 = int(input('Digite o tamanho do segundo lado: '))
l3 = int(input('Digite o tamanho do terceiro lado: '))
if l1+l2 > l3 and l2+l3 > l1 and l1+l3 > l2:
    if l1 == l2 == l3:
        print('Seu triângulo é equilátero.')
    elif l1 != l2 != l3:
        print('Seu triângulo escaleno')
    else:
        print('Seu triângulo é isósceles.')
else:
    print('Não é possível formar um triângulo.')