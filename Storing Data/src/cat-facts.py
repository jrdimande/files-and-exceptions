import json
import requests

url = 'https://meowfacts.herokuapp.com'
response = requests.get(url)

facts = response.json()

with open ('../json/facts.json', 'w') as f:
    json.dump(facts, f, indent=4)
    print('Done!')