num = int(input("Insira um número: "))

inicio = num-5
limite = num+5
salto=1

while(inicio<=limite):

    if(inicio != num):
        print(inicio)
    else:
        print()

    inicio+=salto