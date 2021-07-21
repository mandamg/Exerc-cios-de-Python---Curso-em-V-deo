s = p = 0
while True:
    n = int(input('Digite um numero'))
    if n == 999:
        break
    s += n
    p += 1
print(f'Você digitou {p} numeros, e asoma deles é {s}')