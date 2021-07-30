n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5.0:
    print(f'Sua média foi{media}, você está reprovado.')
elif 7 > media >= 5.0:
    print(f'Sua média foi {media}, você deve fazer recuperação.')
elif media > 7.0:
    print(f'Parabéns, sua média foi {media}. Você foi aprovado.')