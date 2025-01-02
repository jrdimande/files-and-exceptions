import json
filename = 'json/favorite_number.json'
number = int(input("Enter your favorite number: "))

with open(filename,'w') as f:
    json.dump(number, f)
    print("Your favorite numbers was saved")
