num=1
count=-1
somatorio=1

while(num!=-1):
    num=int(input("Insira um número ( -1 para parar ): "))
    count+=1
    somatorio+=num

media=somatorio/count
print("Média:",media)
