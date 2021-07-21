somam = 0
media = 0
hvelho = 0
nvelho = 0
for c in range(1,5):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    sexo = input('digite o sexo').upper()
    media += idade/4 #faz a media da idade
    if idade <= 20 and sexo == 'F':
        somam += 1 #soma quantidade de pessoas com menos de 20 do genero f
    if c == 1 and sexo == 'M':
        hvelho = idade  #mostra idade e nome do homem ais velho
        nvelho = nome
    else:
        if idade > hvelho and sexo == 'M':
            hvelho = idade
            nvelho = nome
print(f'a media das idades é {media}')
print(f'o total de mulheres menores de 20 anos é {somam}')
print(f'O homem mais velho é {nvelho} ele tem {hvelho} anos')