numeros=[]

# Utilizador deve inserir 10 números
for i in range(0, 10):
    num = int(input(f"Insira no numeros [{i}]: "))
    numeros.append(num)

maior=0

for i in range(0, 10):
    if(numeros[i]>maior):
        maior= numeros[i]

print("Maior:",maior)
