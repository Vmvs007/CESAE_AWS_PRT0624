a = int(input("Insira um número: "))
b = int(input("Insira um número: "))
c = int(input("Insira um número: "))

if (a < b and a < c):
    print("Menor:", a)

if (b < a and b < c):
    print("Menor:", b)

if (c < a and c < b):
    print("Menor:", c)
