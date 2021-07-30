a = float(input('Digite sua altura:'))
p = float(input('Digite seu peso:'))
imc = p/(a*a)
if imc < 18.5:
    print(f'IMC: {imc:.1f} está abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc:.1f} está no peso ideal')
elif 25 <= imc < 30:
    print(f'IMC: {imc:.1f} está no sobrepeso')
elif 30 <= imc < 40:
    print(f'IMC: {imc:.1f} está na obesidade')
else:
    print(f'IMC: {imc:.1f} está em obesidade mórbida')