import json
import requests

filename = '/home/vboxuser/files-and-exceptions/Storing Data/json/cat_facts.json'

url = 'https://meowfacts.herokuapp.com'
response = requests.get(url)
facts = response.json()
fact = facts['data'][0]


with open(filename) as f:
    content = json.load(f)

content['data'].append(fact)



with open(filename, 'w') as f:
    json.dump(content, f)


with open(filename) as f:
    content = json.load(f)

for fact in range(len(content['data'])):
    print(content['data'][fact])






