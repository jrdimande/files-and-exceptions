import json

filename = '../json/teste.json'

with open(filename) as f:
    content = json.load(f)

print(content['user']['name'])
print(content['user']['age'])
print(content['user']['heigth'])