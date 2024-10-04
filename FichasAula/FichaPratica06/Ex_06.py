numeros=[]
crescente = True

# Utilizador deve inserir 10 números
for i in range(0, 10):
    num = int(input(f"Insira no numeros [{i}]: "))
    numeros.append(num)

for i in range(1,len(numeros)):
    if(numeros[i]<=numeros[i-1]):
        crescente=False

if(crescente):
    print("Crescente")
else:
    print("Não crescente")