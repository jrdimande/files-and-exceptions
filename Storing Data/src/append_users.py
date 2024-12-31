
import json
import math


filename = 'users.json'

with open(filename) as f:
    content = json.load(f)


while True:

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        heigth = float(input("Enter your heigth: "))

        user = {'name': name, 'age': age, 'heigth' : heigth}

        content['users'].append(user)


        sum = 0


        for age in range(len(content['users'])):
            sum += content['users'][age]['age']


        print(f"Sum is {sum}")
        print(f"The avarage is {math.ceil(sum / len(content['users']))} \n")



        for user in range(len(content['users'])):
            print(content['users'][user]['name'].title())



        with open(filename, 'w') as f:
            json.dump(content, f, indent=3)

