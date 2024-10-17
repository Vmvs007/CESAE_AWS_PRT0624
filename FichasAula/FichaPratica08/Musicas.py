import json

# Carregar o ficheiro JSON com as músicas
with open('musicas.json', 'r') as f:
    musicas = json.load(f)


# Função para pesquisar músicas por género
def pesquisar_por_genero(genero):
    resultado = []
    for musica in musicas:
        if musica["Genero"].lower() == genero.lower():
            resultado.append(musica["Nome da musica"])
    if resultado:
        print(f"Músicas do género {genero}: ", ", ".join(resultado))
    else:
        print(f"Não foram encontradas músicas do género {genero}.")


# Função para pesquisar músicas por artista
def pesquisar_por_artista(artista):
    resultado = []
    for musica in musicas:
        if musica["Artista"].lower() == artista.lower():
            resultado.append(musica["Nome da musica"])
    if resultado:
        print(f"Músicas do artista {artista}: ", ", ".join(resultado))
    else:
        print(f"Não foram encontradas músicas do artista {artista}.")


# Função para encontrar a música com maior duração
def musica_maior_duracao():
    maior_duracao = musicas[0]

    for musica in musicas:
        duracao_atual = int(musica['Duracao'].split(':')[0]) * 60 + int(musica['Duracao'].split(':')[1])
        duracao_maior = int(maior_duracao['Duracao'].split(':')[0]) * 60 + int(maior_duracao['Duracao'].split(':')[1])

        if duracao_atual > duracao_maior:
            maior_duracao = musica

    print(f"A música com maior duração é {maior_duracao['Nome da musica']} ({maior_duracao['Duracao']})")


# Função para encontrar músicas com duração acima de um valor especificado
def pesquisar_duracao_acima(valor_minuto):
    resultado = []

    for musica in musicas:
        duracao = int(musica['Duracao'].split(':')[0]) * 60 + int(musica['Duracao'].split(':')[1])
        if duracao > valor_minuto * 60:
            resultado.append(musica["Nome da musica"])

    if resultado:
        print(f"Músicas com duração acima de {valor_minuto} minutos: ", ", ".join(resultado))
    else:
        print(f"Não foram encontradas músicas com duração acima de {valor_minuto} minutos.")


# Função para contar o número de músicas no ficheiro
def contar_musicas():
    print(f"O número total de músicas é: {len(musicas)}")


# Menu principal
def menu_musicas():
    while True:
        print("\nMenu:")
        print("1. Pesquisar por género")
        print("2. Pesquisar por artista")
        print("3. Música com maior duração")
        print("4. Pesquisar músicas com duração acima de um valor")
        print("5. Número de músicas")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            genero = input("Digite o género: ")
            pesquisar_por_genero(genero)

        elif escolha == "2":
            artista = input("Digite o nome do artista: ")
            pesquisar_por_artista(artista)

        elif escolha == "3":
            musica_maior_duracao()

        elif escolha == "4":
            valor_minuto = int(input("Digite o valor em minutos: "))
            pesquisar_duracao_acima(valor_minuto)

        elif escolha == "5":
            contar_musicas()

        elif escolha == "0":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu_musicas()
