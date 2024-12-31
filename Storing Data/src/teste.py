import json

filename = '../json/teste.json'
info = {'user' : {}}

info['user']['name'] = 'ian'
info['user']['age'] = '14'
info['user']['heigth'] = 1.80

with open(filename, 'w') as f:
    json.dump(info, f)
    print('Done!')

