numeros=[]

# Utilizador deve inserir 10 números
for i in range(0, 10):
    num = int(input(f"Insira no numeros [{i}]: "))
    numeros.append(num)

# Imprimir a lista
for i in range(0, 10):
    print(f"numeros[{i}]: {numeros[i]}")

print(numeros)