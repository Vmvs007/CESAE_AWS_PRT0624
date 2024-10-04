numeros = []
crescente = True

# Utilizador deve inserir 10 números
for i in range(0, 10):
    num = int(input(f"Insira no numeros [{i}]: "))
    numeros.append(num)

maiorPar = -1

for i in range(0, 10):
    if (numeros[i] % 2 == 0):

        if(maiorPar%2!=0):
            maiorPar=numeros[i]

        if(maiorPar%2==0 and numeros[i]>maiorPar):
            maiorPar = numeros[i]


if(maiorPar%2==0):
    print("Maior Par:", maiorPar)
else:
    print("Não há pares")

