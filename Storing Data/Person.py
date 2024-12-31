import json

filename = 'personInfo.json'

person = {}

name = input("Enter your name: ")
age = int(input("Enter your age: "))
heigth = float(input("Enter your heigth: "))
phone_number = int(input("Enter your phone number: "))

person['name'] = name
person['age'] = age
person['heigth'] = heigth
person['phone_number'] = phone_number

with open(filename, 'a') as f:
    json.dump(person, f)
    print("Done!")
