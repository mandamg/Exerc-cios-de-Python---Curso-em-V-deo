v = int(input('Digite o numero que deseja converter:'))
op = int(input('Para qual base deseja converter?\n1. Binário\n2. Hexadecimal\n3. Octal\n'))
if op == 1:
    print(bin(v)[2:])
elif op == 2:
    print(hex(v)[2:])
elif op == 3:
    print(oct(v)[2:])
else:
    print('opção inválida')
