numeros=[]

# Utilizador deve inserir 10 números
for i in range(0, 10):
    num = int(input(f"Insira no numeros [{i}]: "))
    numeros.append(num)

print(numeros)

numeros.sort()

print(numeros)

print("Maior Elemento:",numeros[9])