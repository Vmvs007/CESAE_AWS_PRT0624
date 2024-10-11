import json

f = open('Files/sample7.json')

data = json.load(f)

for i in data['people']:
    print(i)