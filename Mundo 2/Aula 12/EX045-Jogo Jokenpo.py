import random
print('Vamos jogar Jokenpo.')
a=str(input('Pedra, papel ou tesoura?\n').lower())
list = ['pedra', 'papel', 'tesoura']
c = random.choice(list)
if a == c:
    print(f'{c}\nEmpatou! Vamos jogar outra vez.')
elif a== 'pedra' and c == 'tesoura' or a == 'papel' and c =='pedra' or a == 'papel' and c == 'pedra':
    print(f'{c}\nParabéns! Você venceu. Vamos jogar novamente?')
else:
    print(f'{c}\nEu venci! Bom jogo, vamos jogar de novo?')