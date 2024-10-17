import json

# Carregar os ficheiros JSON
with open('Files/minimercado.json', 'r') as f:
    vendas = json.load(f)

with open('Files/login_grandesNegocios.json', 'r') as f:
    contas = json.load(f)


# Função para login
def login():
    tipo_conta = None
    user = input("Insira o nome de utilizador: ")
    password = input("Insira a password: ")
    for conta in contas:
        if conta['utilizador'] == user and conta['password'] == password:
            tipo_conta = conta['tipo_conta']
            break
    if tipo_conta:
        print(f"Login efetuado com sucesso como {tipo_conta}")
    else:
        print("Utilizador ou password incorretos.")
    return tipo_conta


# Funções para as diferentes funcionalidades
def consultar_produtos_disponiveis():
    produtos = []
    for item in vendas:
        if item['produto'] not in produtos:
            produtos.append(item['produto'])
    print("Produtos disponíveis:", ", ".join(produtos))


def consultar_produto_categoria(categoria):
    produtos = []
    for item in vendas:
        if item['tipo_produto'] == categoria:
            produtos.append(item['produto'])
    if produtos:
        print(f"Produtos da categoria {categoria}: ", ", ".join(produtos))
    else:
        print(f"Não há produtos na categoria {categoria}")


def produto_mais_barato():
    mais_barato = vendas[0]

    for item in vendas:
        if item['preco_unitario'] < mais_barato['preco_unitario']:
            mais_barato = item

    return mais_barato


def produto_mais_caro():
    mais_caro = vendas[0]

    for item in vendas:
        if item['preco_unitario'] > mais_caro['preco_unitario']:
            mais_caro = item

    return mais_caro

def adicionar_venda():
    produto = input("Insira o nome do produto: ")
    quantidade = int(input("Insira a quantidade vendida: "))
    preco_unitario = float(input("Insira o preço unitário: "))
    nova_venda = {
        "tipo_produto": input("Insira o tipo do produto: "),
        "produto": produto,
        "quantidade_vendida": quantidade,
        "preco_unitario": preco_unitario
    }
    vendas.append(nova_venda)
    print("Venda adicionada com sucesso.")


def analisar_produto_mais_vendido():
    produto_mais_vendido = vendas[0]

    for item in vendas:
        if item['quantidade_vendida'] > produto_mais_vendido['quantidade_vendida']:
            produto_mais_vendido = item

    print(
        f"Produto que vendeu mais unidades: {produto_mais_vendido['produto']} - {produto_mais_vendido['quantidade_vendida']} unidades")


def analisar_produto_maior_valor():
    produto_maior_valor = vendas[0]

    for item in vendas:
        valor_item = item['quantidade_vendida'] * item['preco_unitario']
        valor_produto = produto_maior_valor['quantidade_vendida'] * produto_maior_valor['preco_unitario']
        if valor_item > valor_produto:
            produto_maior_valor = item

    print(f"Produto que gerou mais valor de vendas: {produto_maior_valor['produto']}")


def total_vendas():
    total = 0
    for item in vendas:
        total += item['quantidade_vendida'] * item['preco_unitario']
    return total

def media_vendas():
    total = total_vendas()
    media = total / len(vendas) if vendas else 0
    return media


# Menu principal
def menu():
    tipo_conta = login()

    if tipo_conta == "ADMIN":
        while True:
            print("\nMenu de Administrador:")
            print("1. Analisar produto mais vendido")
            print("2. Analisar produto com maior valor")
            print("3. Total de vendas")
            print("4. Média das vendas")
            print("0. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                produto = analisar_produto_mais_vendido()
                print(f"Produto que vendeu mais unidades: {produto['produto']} - {produto['quantidade_vendida']} unidades")
            elif escolha == "2":
                produto = analisar_produto_maior_valor()
                print(f"Produto que gerou mais valor de vendas: {produto['produto']}")
            elif escolha == "3":
                total = total_vendas()
                print(f"Total de vendas: {total:.2f}€")
            elif escolha == "4":
                media = media_vendas()
                print(f"Média das vendas: {media:.2f}€")
            elif escolha == "0":
                break

    elif tipo_conta == "FUNC":
        while True:
            print("\nMenu de Funcionário:")
            print("1. Adicionar nova venda")
            print("0. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                adicionar_venda()
            elif escolha == "0":
                break

    elif tipo_conta == None:
        while True:
            print("\nMenu de Cliente:")
            print("1. Consultar produtos disponíveis")
            print("2. Consultar produtos de uma categoria")
            print("3. Consultar produto mais barato e mais caro")
            print("0. Sair")
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                consultar_produtos_disponiveis()

            elif escolha == "2":
                categoria = input("Insira a categoria: ")
                consultar_produto_categoria(categoria)

            elif escolha == "3":
                mais_barato = produto_mais_barato()
                print(f"Produto mais barato: {mais_barato['produto']} - {mais_barato['preco_unitario']:.2f}€")
                mais_caro = produto_mais_caro()
                print(f"Produto mais caro: {mais_caro['produto']} - {mais_caro['preco_unitario']:.2f}€")

            elif escolha == "0":
                break


menu()
