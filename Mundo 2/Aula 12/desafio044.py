p= float(input('Digite o valor do produto:'))
f = int(input("Qual a forma de parcelamento?\n1. à vista no dinheiro/cheque (10% de desconto)"
                  "\n2. à vista no cartão (5% de desconto)\n3. 2x no cartão (sem juros)"
                  "\n4. acima de 3x no cartão (20% de juros)\n"))
if f == 1:
    print(p-(p*0.1))
elif f == 2:
    print(p-(p*0.05))
elif f == 3:
    print('2x de', p/2)
elif f == 4:
    a = float(input('Quantas parcelas?\n'))
    print(f'{a:.0f}x de {((p*1.2)/a):.2f}')
else:
    print('opção inválida.')
