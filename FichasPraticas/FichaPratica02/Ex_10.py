num1 = float(input("Insira 1º número: "))
num2 = float(input("Insira 2º número: "))

operacao = input("Operação Aritmética (+ - * /): ")

if (operacao == "+"):
    resultado = num1 + num2
    print("Soma: ", resultado)

if (operacao == "-"):
    resultado = num1 - num2
    print("Subtração: ", resultado)

if (operacao == "*"):
    resultado = num1 * num2
    print("Multiplicação: ", resultado)

if (operacao == "/"):
    resultado = num1 / num2
    print("Divisão: ", resultado)
