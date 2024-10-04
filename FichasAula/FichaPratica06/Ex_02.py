comissoes =[]
total=0

# Utilizador deve inserir 12 números
for i in range(0, 12):
    num = float(input(f"Insira na lista de comissoes [{i}]: "))
    comissoes.append(num)

# Calcular o total
for i in range(0, 12):
    total += comissoes[i]   # total = total + comissoes[i]

print("Total:",total)