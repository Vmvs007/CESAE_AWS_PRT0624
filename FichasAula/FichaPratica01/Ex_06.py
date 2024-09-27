valor1 = int(input("Insira o 1º valor: "))
valor2 = int(input("Insira o 2º valor: "))

print("_________________________________")
print("Valor1:", valor1)
print("Valor2:", valor2)

print("_________________________________")
print("A trocar variáveis...")

valor1 = valor1 + valor2
valor2 = valor1 - valor2
valor1 = valor1 - valor2

print("_________________________________")
print("Valor1:", valor1)
print("Valor2:", valor2)