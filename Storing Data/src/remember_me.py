import json

username = input("What's your name? ")

filename = 'json/username.json'

with open(filename, 'w') as f:
    json.dump(username, f)

    print(f"We will remember you when you come back, {username}")