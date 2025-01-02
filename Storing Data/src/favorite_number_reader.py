import json

filename = 'json/favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
        print(f"Your favorite number is {number}")

except FileNotFoundError:
    print(f"The file {filename} does not exist")