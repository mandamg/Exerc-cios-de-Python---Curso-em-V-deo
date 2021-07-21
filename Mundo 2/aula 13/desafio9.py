from datetime import date
d = date.today().year #peguei a data de hj
tma = 0 #o total começa em 0
tme = 0
for c in range(1,8): #refaz as operaçoes dentro do laço 7 vzs
    n = int(input('digite o ano de nascimento:')) #recebe a data de nasc (deve ser int )
    i = d - n #calculo da idade
    if i >= 18:
        tma += 1 #sempre que uma pessoa for maior irá somar 1
    else:
        tme += 1 #sempre que uma pessoa for menor irá somar 1
print(f'{tma} são maiores')
print(f'{tme} ainda n atingiram a maioridade')