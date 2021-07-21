m = 'S'
soma = p = 0
maior = menor = 0
while m in 'S':
    n = int(input('Digite o numero: '))
    p+=1
    soma += n
    if p == 1:
        maior = menor = n
    else:
        if maior < n:
                maior = n
        if menor > n:
                menor = n
    m = input('Quer continuar/ [S/N]').upper()
print(f'O total de numeros selecionados foi {p}. A soma é {soma}. A média é {soma/p:.2f}. O maior é {maior}, o menor é {menor}.')