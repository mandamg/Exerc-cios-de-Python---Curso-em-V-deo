v = float(input('Qual o valor da casa?'))
a = float(input('Em quantos anos será financiada?'))
s = float(input('Informe seu sálario:'))
p = v/(a*12)
pc = s*0.3
if p <= pc:
    print(f'O valor de suas parcelas ficará {p:.2f}.\nEmprestimo aprovado.')
else:
    print(f'Desculpe, o valor da parcela é {p:.2f}, o que excede 30% do seu sálario. Portanto, seu emprestimo foi negado.')