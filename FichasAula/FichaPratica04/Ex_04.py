num = int(input("Insira um número: "))
primo = True

for i in range(2, num):
    if(num%i==0):
        primo=False

if primo:
    print("Primo")
else:
    primo("Não Primo")

