nome = input('Digite um nome completo:')
print(f'Seu nome em maiúsculas {nome.upper()}')
print(f'Seu nome em minúsculas {nome.lower()}')
divisor = nome.split()
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras.')
print(f'Seu primeiro nome ({divisor[0]}) tem {len(divisor[0])}')