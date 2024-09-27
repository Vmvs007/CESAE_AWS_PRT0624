vezes = int(input("Quantos números deseja inserir: "))
crescente = True
count = 1

anterior = int(input("Insira um número: "))

while (count < vezes):
    atual = int(input("Insira um número: "))
    count += 1

    if(atual<=anterior): # quebra de sequência crescente
        crescente=False

    anterior=atual

if(crescente):
    print("Crescente")
else:
    print("Não crescente")

