tabela = ('Bragantino', 'Athletico - PR', 'Fortaleza', 'Bahia',
          'Palmeiras', 'Atlético - GO', 'Atlético - MG', 'Flamengo', 'Fluminnse',
          'Santos', 'Corinthians', 'Ceará', 'Internacional', 'Juventude', 'Sport',
          'Cuiabá', 'São Paulo', 'Chapecoense', 'América - MG', 'Grêmio')
print('-'*50)
print(f'\033[2;44mos cinco primeiros colocados são:\033[m {tabela[:5]}')
print('-'*50)
print(f'\033[2;43mOs quatro ultimos são:\033[m {tabela[-4:]}')
print('-'*50)
print(f'\033[2;42mem ordem alfabetica\033[m  {sorted(tabela)}')
print('-'*50)
print(f'\033[2;47mA Chapecoense está na {tabela.index("Chapecoense")+1}ª posição\033[m')
for c, pos in enumerate(tabela):
    print(f'\033[2;45mNome:\033[m {pos} \033[2;46mposição:\033[m {c+1}')
print('-'*50)