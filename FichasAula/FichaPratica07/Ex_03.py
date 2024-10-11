listaContactos = []

opcao = 0

while (opcao != 4):
    print("\n******* Lista de Contactos *******")
    print("1. Adicionar Novo Contacto")
    print("2. Consultar Lista de Contactos")
    print("3. Pesquisar um Contacto")
    print("4. Sair")
    opcao = int(input("Opção desejada: "))

    match (opcao):
        case 1:
            print("\nAdicionar Novo Contacto")

            nome = input("Nome: ")
            telemovel = input("Telemovel: ")
            morada = input("Morada: ")

            novoContacto = {
                "nome": nome,
                "telemovel": telemovel,
                "morada": morada
            }

            listaContactos.append(novoContacto)

        case 2:
            print("\nConsultar Lista de Contactos")

            for i in range(0, len(listaContactos)):
                print("_________________________________________________________")
                print(
                    f"Nome: {listaContactos[i]["nome"]}\t|\tTelemovel: {listaContactos[i]["telemovel"]}\t|\tMorada: {listaContactos[i]["morada"]}")

            print("_________________________________________________________")
        case 3:
            print("\nPesquisar um Contacto")

            pesquisa = input("Insira o nome a pesquisar: ")

            for i in range(0, len(listaContactos)):
                if (pesquisa == listaContactos[i]["nome"]):
                    print(
                        f"Telemovel: {listaContactos[i]["telemovel"]}\t|\tMorada: {listaContactos[i]["morada"]}")

        case 4:
            print("\nA sair...")

        case _:
            print("\nOpção não reconhecida...")
