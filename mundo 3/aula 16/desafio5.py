lista = ('Pão', 0.40, 'Presunto', 14, 'Suco', 0.70, 'Mussarela', 20, 'Manteiga', 5)
v ='LISTA DE PREÇO'
print('-'*35)
print(f'{v:^35}')
print('-'*35)
for c in range (0,len(lista), 2):
    print(f'{lista[c]:.<30}', end= '')
    print(f'R$ {lista[c+1]:>}')
print('-'*35)