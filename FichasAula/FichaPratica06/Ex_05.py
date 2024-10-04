numeros = []

num = 1
soma = 0

while (num >= 0):
    num = int(input("Insira um numero (negativo para parar): "))
    if (num >= 0):
        numeros.append(num)

for i in range(0, len(numeros)):
    soma += numeros[i]

#for i in numeros:
#    soma += i

media = soma/len(numeros)
print("Media:",media)
