import json

filename = '/Storing Data/json/cat_facts.json'

try:
    with open(filename, 'r') as f:
        content = json.load(f)
except FileNotFoundError:
    print(f"The file {filename} does not exist")
else:
    print(content)