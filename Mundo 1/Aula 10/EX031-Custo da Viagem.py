n = int(input('Digite a distancia da viagem em Km'))
if n<=200:
    print(f'a passagem vai custar {n*0.50}')
else:
    print(f'A passagem vai custar {n*0.45}')