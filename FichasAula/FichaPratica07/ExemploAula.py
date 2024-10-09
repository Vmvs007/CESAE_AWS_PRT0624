# Criação do dicionário
animais = {
    "a": "Avestruz",
    "b": "Bisonte",
    "c": "Coruja"
}

# Imprimir um dicionário
print("1:",animais)

# Imprimir um determinado elemento
print("2:",animais["b"])

# Adicionar um novo elemento
animais["d"] = "Doninha"

print("3:", animais)

# Reatribuir um valor
animais["d"] = "Dromedario"

print("4:", animais)

# Mostrar todas as keys
print("5:",animais.keys())

# Mostrar todos os valores
print("6:",animais.values())

# Criar uma lista a partir dos values de um dicionário
umaLista = list(animais.values())
print("7:",umaLista)

# Buscar um valor
print("8:",animais.get("r"))

# Criar um dicionário de lista
dicionarioAnimais={
    "a":["Avestruz","Andorinha"],
    "b":["Bisonte","Baleia"]
}

# Imprimir o tipo de dados de uma key
print("9:",type(dicionarioAnimais["b"]))

# Juntar um elemento à lista da key "a"
dicionarioAnimais["a"].append("Alpaca")
print("10:", dicionarioAnimais)

# Adicionar uma nova key ao dicionário com lista
if "c" not in dicionarioAnimais:
    dicionarioAnimais["c"]=[]

dicionarioAnimais["c"].append("Coruja")
print("11:", dicionarioAnimais)