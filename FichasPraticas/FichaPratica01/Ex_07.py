preco1 = float(input("Insira o preço 1: "))
preco2 = float(input("Insira o preço 2: "))
preco3 = float(input("Insira o preço 3: "))

total = preco1 + preco2 + preco3
# totalComDesconto = total - (total * 0.1)
totalComDesconto = total * 0.9

print("Valor Total:", total)
print("Valor Total com 10% de Desconto:", totalComDesconto)
