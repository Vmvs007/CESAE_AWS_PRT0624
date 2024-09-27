inicio = 0
limite = 100
salto = 1
somatorio=0

while(inicio<=limite):
    print(inicio)
    somatorio+=inicio
    inicio+=salto

print("Somatório:",somatorio)