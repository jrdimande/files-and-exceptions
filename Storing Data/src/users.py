import json
filename = '../json/users.json'
data = {'users': []}


name = input("Enter your name: ")
age = int(input("Enter your age: "))
heigth = float(input("Enter your heigth: "))

user = {'name': name, 'age': age, 'heigth' : heigth}

data['users'].append(user)


with open(filename,'w') as f:
    json.dump(data, f)

