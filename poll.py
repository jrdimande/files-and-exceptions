from click import prompt
from speechd_config import question

filepath = '/home/vboxuser/files-and-exceptions/txts/responses.txt'
flag = True

while flag:
    name = input('Enter your name: ')
    if name != '0':
        response = input(f'Why do you like programming?\na: ')

        with open(filepath, 'a') as file_object:
            file_object.write(f'\n{name.title()}: {response}')
    else:
        flag = False

