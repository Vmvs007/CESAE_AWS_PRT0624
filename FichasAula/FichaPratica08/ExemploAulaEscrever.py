import json


dicionarioCompleto=[]

with open('informacoes.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
    dicionarioCompleto.append(data)

nomeUser = input("Insira o seu nome: ")

dicionarioNovo = {
    "nome": nomeUser,
    "idade": 25,
    "telemovel": 911222333,
    "morada": "Porto"
}

dicionarioCompleto.append(dicionarioNovo)


with open('informacoes.json','w',encoding='utf-8') as outfile:
    json.dump(dicionarioCompleto,outfile)

