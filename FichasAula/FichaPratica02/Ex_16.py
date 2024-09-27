valor= int(input("Insira o valor (euros): "))

# Notas de 200
notas = valor//200
print("Notas de 200€:",notas)

valor=valor%200

# Notas de 100
notas = valor//100
print("Notas de 100€:",notas)

valor=valor%100

# Notas de 50
notas = valor//50
print("Notas de 50€:",notas)

valor=valor%50

# Notas de 20
notas = valor//20
print("Notas de 20€:",notas)

valor=valor%20

# Notas de 10
notas = valor//10
print("Notas de 10€:",notas)

valor=valor%10

# Notas de 5
notas = valor//5
print("Notas de 5€:",notas)