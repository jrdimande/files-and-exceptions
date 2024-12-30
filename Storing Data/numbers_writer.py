import json

numbers = [1, 3, 7, 9, 11, 13]

filename = '../../.config/JetBrains/PyCharmCE2024.3/scratches/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)