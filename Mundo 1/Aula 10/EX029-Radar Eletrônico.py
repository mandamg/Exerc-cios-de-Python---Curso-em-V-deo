v = int(input('Qual a velocidade do carro?'))
print(f'Vocâ foi multado em R${(v-80)*7}' if v>80 else 'Não possui multa.')
print('Dirija com cuidado!')