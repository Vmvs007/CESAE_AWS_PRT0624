salario = float(input("Insira o salário anual: "))

if (salario <= 15000):
    imposto = salario * 0.2
    print("Imposto de 20%:", imposto)
elif (salario > 15000 and salario <= 20000):
    imposto = salario * 0.3
    print("Imposto de 30%:", imposto)
elif (salario > 20000 and salario <= 25000):
    imposto = salario * 0.35
    print("Imposto de 35%:", imposto)
else:
    imposto = salario * 0.4
    print("Imposto de 40%:", imposto)
