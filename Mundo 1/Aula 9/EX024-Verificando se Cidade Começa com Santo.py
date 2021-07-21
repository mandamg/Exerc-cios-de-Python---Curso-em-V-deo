#n = str(input('digite o nome de sua cidade'))
#d# = n.split()
#m #= d[0].upper().find('SANTO')
#if m < 0:
#    print('Sua cidade não possui "Santo" no primeiro nome')
#if m >= 0:
#    print('Sua cidade possui "Santo" no primeiro nome')
n = str(input('digite o nome da cidade:')).strip().upper()
print(n[0:5]=='SANTO')