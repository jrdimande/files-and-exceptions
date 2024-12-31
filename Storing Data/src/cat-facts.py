import json
import requests

filename = '/home/vboxuser/files-and-exceptions/Storing Data/json/cat-facts.json'

url = 'https://meowfacts.herokuapp.com'
response = requests.get(url)
facts = response.json()

with open(filename, 'w') as f:
    json.dump(facts, f)




