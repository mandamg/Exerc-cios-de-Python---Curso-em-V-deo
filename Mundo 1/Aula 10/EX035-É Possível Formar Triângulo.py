t1 = float(input('Digite o comprimento do primeiro lado:'))
t2 = float(input('Digite o comprimento do segundo lado:'))
t3 = float(input('Digite o comprimento do terceiro lado:'))
if (t1+t2) > t3 and (t3+t2) > t1 and (t1+t3) > t2:
    print('\033[1;31;40mÉ possivel formar um triângulo\033[m')
else:
    print('\033[1,31Não é possivel formar um triângulo')