print('Bem vindo a Loja do Eduardo ★')
valorUnitario = float(input('Valor unitário: '))
qntProduto = float(input('Quantidade do produto: '))
valorTotal = valorUnitario * qntProduto
if qntProduto <= 4:
    valorFinal = valorTotal
elif 5 <= qntProduto < 19:
    valorFinal = valorTotal - valorTotal * 0.03
elif 20 <= qntProduto < 99:
    valorFinal = valorTotal - valorTotal * 0.06
else:
    valorFinal = valorTotal - valorTotal * 0.10

print('Valor sem desconto R${}'.format(valorTotal))
print('Valor com desconto R${}'.format(valorFinal))
