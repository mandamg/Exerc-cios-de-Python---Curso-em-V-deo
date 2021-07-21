f = str(input('digite ')).strip().lower().split()
d = ''.join(f)
i = ''
for fr in range (len(d)-1,-1,-1):
    i += d[fr]
if i == d:
    print(f'O termo é palindromo')
else:
    print('não é palindromo')
print(len(d)-1)
print(i)

