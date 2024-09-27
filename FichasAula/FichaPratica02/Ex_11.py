saldo = float(input("Insira o saldo atual: "))
movimento = float(input("Insira o montante a debitar/creditar: "))

if(saldo+movimento<0): # não permitido
    print("Operação Inválida. Saldo Insuficiente")
else:
    saldo = saldo + movimento

print("Saldo Final:",saldo)

