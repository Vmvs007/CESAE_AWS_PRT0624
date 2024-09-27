totalSegundosAlbum = 0

minMusica = int(input("Insira os minutos da música 1: "))
segMusica = int(input("Insira os segundos da música 1: "))

totalSegundosAlbum = totalSegundosAlbum + (minMusica * 60) + segMusica

minMusica = int(input("Insira os minutos da música 2: "))
segMusica = int(input("Insira os segundos da música 2: "))

totalSegundosAlbum = totalSegundosAlbum + (minMusica * 60) + segMusica

minMusica = int(input("Insira os minutos da música 3: "))
segMusica = int(input("Insira os segundos da música 3: "))

totalSegundosAlbum = totalSegundosAlbum + (minMusica * 60) + segMusica

horas = totalSegundosAlbum // 3600
minutos = (totalSegundosAlbum // 60) - (horas * 60)
segundos = totalSegundosAlbum - (horas * 3600) - (minutos * 60)

print(horas, ":", minutos, ":", segundos)
