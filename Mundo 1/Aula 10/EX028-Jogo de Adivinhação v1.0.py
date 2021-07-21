from random import randint
from playsound import playsound
from time import sleep
print('-=-'*15)
print(' TENTE DESCOBRIR O NUMERO QUE EU VOU PENSAR!')
print('-=-'*15)
sleep(1.5)
print('...')
sleep(3)
us = input('Que numero numero que eu pensei?')
num = randint(0, 5)
if num == us:
    print('Parabéns! você acertou.')
else:
    print(f'Eu pensei no numero {num}.\nVocê errou. Tente novamente.')
    playsound('silvio.mp3')
