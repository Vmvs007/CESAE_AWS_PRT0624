from FichaPratica05.Ex_06 import numeroPar, numeroPositivo, primo

numero = int(input("Insira um número: "))
opcao = 0

while (opcao != 7):
    print("\n\n***** Programa de Análise de um Número:", numero, "*****")
    print("1. Par ou Impar")
    print("2. Positivo ou Negativo")
    print("3. Primo ou Não Primo")
    print("4. Perfeito ou Não Perfeito")
    print("5. Triangular ou Não Triangular")
    print("6. Trocar de Número")
    print("7. Sair")
    print("********************************************************")

    opcao = int(input("Insira a opção: "))

    match (opcao):
        case 1:  # Par ou Impar

            if(numeroPar(numero)):
                print("Par")
            else:
                print("Impar")

        case 2:  # Positivo ou Negativo

            if (numeroPositivo(numero)):
                print("Positivo")
            else:
                print("Negativo")

        case 3:  # Primo ou Não Primo

            if (primo(numero)):
                print("Positivo")
            else:
                print("Negativo")


        case 4:  # Perfeito ou Não Perfeito
            print()

        case 5:  # Triangular ou Não Triangular
            print()

        case 6:  # Trocar de Número
            print()

        case 7:  # Sair
            print("\n!!! Obrigado !!!")

