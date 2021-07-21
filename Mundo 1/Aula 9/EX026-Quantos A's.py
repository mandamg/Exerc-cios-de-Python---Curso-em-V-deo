frase = input('Digite uma frase: ').upper().strip()
n = frase.count('A')
m = frase.find('A')+1
o = frase.rfind('A')+1
print(f"sua frase possui {n} A's\nO primeiro esta na posição {m}\nO ultimo esta na posição {o}")