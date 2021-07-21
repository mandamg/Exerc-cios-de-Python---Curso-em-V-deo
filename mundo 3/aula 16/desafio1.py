n = int(input('Digite o valor entre 0 a 20:'))
numero = ('zero', 'um', 'dois', 'três','quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while not n < 20 and 0 < n:
    n = int(input('Valor inválido. Digite um numero entre 0 e 20:'))
print(numero[n])
