n = int(input('Digite um numero para ver a ssequencia'))
r = int(input('digite a razão'))
f = n
p = 0
total = 0
mais = 10
while mais != 0:
        total+= mais
        while p <= total:
                print(f'{f}->', end='')
                f += r
                p += 1
        mais = int(input('Quantos a mais vc quer?'))
print('Fim')
print(total)